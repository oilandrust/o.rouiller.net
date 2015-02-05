from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.PostList.as_view(), name='blog'),  
    url(r'^(?P<slug>\S+)$', views.PostDetail.as_view(), name='post'),
)
