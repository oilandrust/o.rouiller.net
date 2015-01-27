from django.db import models
from django.core.urlresolvers import reverse
from django_markdown.models import MarkdownField

class ProjectQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

class Project(models.Model):
    name = models.CharField(max_length=200)
    
    short_description = models.TextField()
    description = MarkdownField(blank=True)
    
    
    published = models.BooleanField(default=True)
    date = models.DateField(blank=True)
    type = models.CharField(max_length=50)
    thumbnail = models.ImageField(blank=True)
    link = models.URLField(blank=True)

    slug = models.SlugField(max_length=200, unique=True)

    objects = ProjectQuerySet.as_manager()

    def __str__(self):
        return self.name
    
    @property
    def page_url(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        if self.link:
            return self.link
        return reverse('project_detail', kwargs={"slug":self.slug})

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-date"]
