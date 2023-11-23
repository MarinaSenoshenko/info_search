from django.db import IntegrityError
from django.http import HttpResponseNotFound, JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from . import student_forms, student_models, university_forms, university_models
import json
import datetime


# Maina admin
def main(request):
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        small_name = request.POST.get("small_name")
        date = request.POST.get("date")
        name = request.POST.get("name")
        university = request.POST.get("university")
        year = request.POST.get("year")

        if full_name and small_name and date:
            latest_university = university_models.University.objects.latest('id')
            new_id = latest_university.id + 1 if latest_university else 1
            university_models.University.objects.create(id=new_id,
                                                        full_name=full_name,
                                                        small_name=small_name,
                                                        date=date)

        if name and date and university and year:
            latest_student = student_models.Student.objects.latest('id')
            new_id = latest_student.id + 1 if latest_student else 1
            student_models.Student.objects.create(id=new_id,
                                                  name=name,
                                                  date=date,
                                                  university=university,
                                                  year=year)
        return redirect('/')
    else:
        all_students = student_models.Student.objects.all()
        all_universities = university_models.University.objects.all()
        data = {"students": all_students,
                "universities": all_universities,
                "student_form": student_forms.StudentForm(),
                "university_form": university_forms.UniversityForm()}
    return render(request, 'main/main_page.html', data)


def update_student(request, student_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        field_name = data.get('field')
        new_value = data.get('value')

        student = student_models.Student.objects.get(id=student_id)

        try:
            if field_name == 'name':
                student.name = new_value
            elif field_name == 'date_born':
                new_value = new_value.replace('.', '')
                if len(new_value) > 3 and new_value[3] != ' ':
                    new_value = new_value[:3] + new_value[4:]
                student.date = datetime.datetime.strptime(new_value, "%b %d, %Y").strftime("%Y-%m-%d")
            elif field_name == 'university':
                student.university = new_value
            elif field_name == 'year':
                student.year = new_value
        except ValueError:
            pass

        student.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def update_university(request, university_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        field_name = data.get('field')
        new_value = data.get('value')

        university = university_models.University.objects.get(id=university_id)

        if field_name == 'full_name':
            university.full_name = new_value
        elif field_name == 'small_name':
            university.small_name = new_value
        elif field_name == 'date_create':
            new_value = new_value.replace('.', '')
            if len(new_value) > 3 and new_value[3] != ' ':
                new_value = new_value[:3] + new_value[4:]
            try:
                university.date = datetime.datetime.strptime(new_value, "%b %d, %Y").strftime("%Y-%m-%d")
            except ValueError:
                pass

        university.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def delete_student(request, student_id):
    try:
        student_for_delete = student_models.Student.objects.get(id=student_id)
        student_for_delete.delete()
        return redirect('/')
    except student_models.Student.DoesNotExist:
        return HttpResponseNotFound("Student with this id is not exists")


def delete_university(request, university_id):
    try:
        university_for_delete = university_models.University.objects.get(id=university_id)
        university_for_delete.delete()
        return redirect('/')
    except university_models.University.DoesNotExist:
        return HttpResponseNotFound("University with this id does not exist")
    except IntegrityError:
        return HttpResponse("Cannot delete the university. There are references to it in the student table.")
