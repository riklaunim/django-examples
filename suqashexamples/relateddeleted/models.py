from django.db import models


class NewCategory(models.Model):
    title = models.CharField(max_length=100)


class News(models.Model):
    title = models.CharField(max_length=100)
    new_category = models.ForeignKey(NewCategory, blank=True, null=True)

