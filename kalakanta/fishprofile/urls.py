from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^myprofile/$', views.myprofile, name='myprofile'),
    url(r'^addfish/$', views.addfish, name='addfish'),
    url(r'^api/myfish/$', views.queryfish, name='queryfish'),
    url(r'^api/mapquery/$', views.mapquery, name='mapquery'),
]
