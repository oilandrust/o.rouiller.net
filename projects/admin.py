from django.contrib import admin
from projects import models

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','date')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(models.Project, ProjectAdmin)
