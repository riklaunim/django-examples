from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=(('m', 'm'), ('f', 'f')), default='m', max_length=1)

    class Meta:
        unique_together = ('first_name', 'last_name')
