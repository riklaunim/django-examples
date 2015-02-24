from urllib.parse import urljoin

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    cover_image = models.ImageField(upload_to='covers/')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        path = reverse('post', kwargs={'pk': self.id})
        return urljoin(settings.BASE_URL, path)
