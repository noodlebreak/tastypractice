from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from myapp.api import EntryResource, UserResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())

urlpatterns = patterns('',
    # The normal jazz here...
    url(r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('myapp.urls')),
    (r'^api/', include(v1_api.urls)),
)
