# myapp/api.py
from django.contrib.auth.models import User

from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from myapp.models import Entry


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        fields = ['email','is_superuser','is_active','username']
        filtering = {
            'username': ALL,
        }


class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        allowed_methods = ["get"]
        # excludes = ['id','slug','pub_date']
        fields = ['user','title','body','pub_date']

        filtering = {
            'user': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }