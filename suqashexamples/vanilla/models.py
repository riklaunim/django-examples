from django.db import models


class News(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

