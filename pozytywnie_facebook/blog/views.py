from django.template.defaultfilters import striptags
from django.template.defaultfilters import truncatewords
from django.views import generic

import social_metadata.views

from blog import models


class HomeView(generic.ListView):
    def get_queryset(self):
        return models.Post.objects.all().order_by('-posted_date')

home_view = HomeView.as_view()


class PostView(social_metadata.views.SocialDataMixin, generic.DetailView):
    model = models.Post

    def get_social_title(self):
        return self.object.title

    def get_social_images(self):
        yield self.object.cover_image.url

    def get_social_description(self):
        return truncatewords(striptags(self.object.text), 50)


post_view = PostView.as_view()
