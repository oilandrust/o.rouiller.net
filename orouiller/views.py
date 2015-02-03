from django.shortcuts import render
from projects.models import Project

def home(request):  

    projects = Project.objects.exclude(type='publication')
    recent = projects.exclude(old=True)

    old_list = list(projects.filter(old=True))
    old_list_1 = old_list[::2]
    old_list_2 = old_list[1::2]

    publications = Project.objects.filter(type='publication')

    return render(request, 'orouiller/home.html', 
                            {
                                'projects':recent,
                                'old_projects_1':old_list_1,
                                'old_projects_2':old_list_2,
                                'publications':publications,
                            })
