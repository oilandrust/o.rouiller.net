from django.shortcuts import render
from projects.models import Project

def home(request):  

    projects = Project.objects.exclude(type='publication')
    publications = Project.objects.filter(type='publication')

    return render(request, 'orouiller/home.html', 
                            {
                                'projects':projects,
                                'publications':publications,
                            })
