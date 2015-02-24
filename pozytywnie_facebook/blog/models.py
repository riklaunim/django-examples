from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    cover_image = models.ImageField(upload_to='covers/')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
