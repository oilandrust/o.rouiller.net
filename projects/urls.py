from django.conf.urls import patterns, include, url
from projects import views

urlpatterns = patterns('',
   
    url(r'^(?P<slug>\S+)$', views.ProjectDetail.as_view(), name='project_detail'),

)
