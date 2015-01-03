from django.views import generic
from rest_framework import viewsets

from blog import models
from blog import serializers


class HomeView(generic.ListView):
    def get_queryset(self):
        return models.Post.objects.all().order_by('-posted_date')

home_view = HomeView.as_view()


class CategoryPosts(generic.DetailView):
    model = models.Category
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryPosts, self).get_context_data(**kwargs)
        context['post_list'] = self._get_posts()
        return context

    def _get_posts(self):
        category = self.object
        return (models.Post.objects.filter(category_id=category.id)
                .order_by('-posted_date'))

category_posts = CategoryPosts.as_view()


class PostView(generic.DetailView):
    model = models.Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['is_python'] = self._get_is_python()
        return context

    def _get_is_python(self):
        return ('python' in self.object.category.name.lower()
                or 'python' in self.object.title)

post_view = PostView.as_view()


class CategorySetView(viewsets.ReadOnlyModelViewSet):
    model = models.Category
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.all()


class PostSetView(viewsets.ReadOnlyModelViewSet):
    model = models.Post
    serializer_class = serializers.PostSerializer
    filter_fields = ('category', )
    queryset = models.Post.objects.all()
