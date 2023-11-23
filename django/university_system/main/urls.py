from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('delete_student/<int:student_id>/', views.delete_student),
    path('delete_university/<int:university_id>/', views.delete_university),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('update_university/<int:university_id>/', views.update_university, name='update_university'),
]
