from django.views import generic
from projects import models

class ProjectDetail(generic.DetailView):
    model = models.Project
    template_name = 'projects/project.html'

 
