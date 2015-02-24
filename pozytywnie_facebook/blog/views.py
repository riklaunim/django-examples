from django.views import generic

from blog import models


class HomeView(generic.ListView):
    def get_queryset(self):
        return models.Post.objects.all().order_by('-posted_date')

home_view = HomeView.as_view()


class PostView(generic.DetailView):
    model = models.Post

post_view = PostView.as_view()
