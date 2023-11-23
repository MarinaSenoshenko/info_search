from django.db import models


class University(models.Model):
    full_name = models.CharField()
    small_name = models.CharField()
    date = models.DateField()

    class Meta:
        db_table = 'university'
