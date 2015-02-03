from django.shortcuts import render
from projects.models import Project

def home(request):  

    projects = Project.objects.exclude(type='publication')
    recent = projects.exclude(old=True)
    old = projects.filter(old=True)


    publications = Project.objects.filter(type='publication')

    return render(request, 'orouiller/home.html', 
                            {
                                'projects':recent,
                                'old_projects':old,
                                'publications':publications,
                            })
