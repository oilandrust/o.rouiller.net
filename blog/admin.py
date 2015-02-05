from django.contrib import admin
from blog import models
from django_markdown.admin import MarkdownModelAdmin


class PostAdmin(MarkdownModelAdmin):
    list_display = ('title','created')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
