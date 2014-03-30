from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

from quotes import resources
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(resources.UserResource())
v1_api.register(resources.QuoteResource())

urlpatterns = patterns(
    '',
    url(r'^$', 'quotes.views.main_page'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
