from django.conf.urls import patterns, include, url
from myapp.api import EntryResource

entry_resource = EntryResource()

urlpatterns = patterns('', 
	url(r'^$','myapp.views.home'),    
    url(r'^api/', include(entry_resource.urls)),
)