from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    category = models.ForeignKey(Category)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
