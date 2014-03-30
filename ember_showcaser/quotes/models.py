from django.db import models


class Quote(models.Model):
    quote = models.CharField(max_length=300, unique=True)
    poster = models.ForeignKey('auth.user')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.quote
