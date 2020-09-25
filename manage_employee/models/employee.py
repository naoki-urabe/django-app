from django.db import models

class Employee(models.Model):
    class Meta:
        db_table = 'employee'
    name = models.CharField(verbose_name='名前', max_length=10)
    age = models.IntegerField(verbose_name='年齢')