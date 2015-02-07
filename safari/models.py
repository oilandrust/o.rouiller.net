from django.db import models



class TinderImage(models.Model):
    image = models.ImageField()

    uploaded = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return self.image.url

    def __str__(self):
        return str(self.uploaded)

