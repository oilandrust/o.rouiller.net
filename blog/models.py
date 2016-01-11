from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse

from projects.models import Project

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(blank=True, max_length=200)

    def get_absolute_url(self):
        return self.image.url

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=200)
    content = MarkdownField(blank = True)

    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default = True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = PostQuerySet.as_manager()

    project = models.ForeignKey(Project, null = True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug":self.slug})


    class Meta:
        ordering = ["-created"]
