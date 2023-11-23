from django.db import models


class Student(models.Model):
    name = models.CharField()
    date = models.DateField()
    university = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        db_table = 'student'
