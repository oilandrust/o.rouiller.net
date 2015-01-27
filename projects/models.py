from django.db import models


class ProjectQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    published = models.BooleanField(default=True)
    date = models.DateField()
    type = models.CharField(max_length=50)

    objects = ProjectQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-date"]
