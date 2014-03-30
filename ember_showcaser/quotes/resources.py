from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.http import HttpUnauthorized
from tastypie.resources import fields
from tastypie.resources import ImmediateHttpResponse
from tastypie.resources import ModelResource

from quotes import models


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get']
        always_return_data = True
        fields = ['username']


class QuoteResource(ModelResource):
    poster = fields.ForeignKey(UserResource, 'poster')

    class Meta:
        queryset = models.Quote.objects.all()
        allowed_methods = ['get', 'post']
        always_return_data = True
        authorization = Authorization()

    def obj_create(self, bundle, **kwargs):
        if bundle.request.user.is_authenticated():
            return super(QuoteResource, self).obj_create(bundle,
                                                         poster=bundle.request.user,
                                                         **kwargs)
        raise ImmediateHttpResponse(HttpUnauthorized('Not authenticated'))
