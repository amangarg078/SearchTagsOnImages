from django.conf.urls import url

from . import views
#app_name = 'searchengine'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$',views.imageDetails, name='imagedetails'),
    url(r'^(?P<model>\w+)/$',views.tagDetails, name='tagdetails'),
    ]
