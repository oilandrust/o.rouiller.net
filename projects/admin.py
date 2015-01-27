from django.contrib import admin
from projects import models
from django_markdown.admin import MarkdownModelAdmin

class ProjectAdmin(MarkdownModelAdmin):
    list_display = ('name','date')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(models.Project, ProjectAdmin)
