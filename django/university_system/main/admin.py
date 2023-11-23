from django.contrib import admin

from . import student_models, university_models

admin.site.register(student_models.Student)
admin.site.register(university_models.University)
