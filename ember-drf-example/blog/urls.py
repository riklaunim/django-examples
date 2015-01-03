from django.conf.urls import patterns, url


urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'home_view', name='posts'),
    url(r'^category/(?P<pk>[0-9]+)/$', 'category_posts', name='category-posts'),
    url(r'^(?P<slug>[\w\-_]+)/$', 'post_view', name='post'),
)
