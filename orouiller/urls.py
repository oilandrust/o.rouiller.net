from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = patterns('',
   
    url(r'^blog/', include('blog.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^$', 'orouiller.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),


    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
       {'template_name': 'safari/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'), 

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
