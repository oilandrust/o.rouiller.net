from django.conf.urls import patterns, include, url
from safari import views

urlpatterns = patterns('',
   
    url(r'^$', views.TinderImages.as_view(), name='tinder_safari'),
    url(r'^upload/$', views.upload, name='upload'),
)
