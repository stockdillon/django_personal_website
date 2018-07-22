from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)


class Result(models.Model):
    objects = models.Manager() # This was added to prevent a pylint warning in VSC... not necessary
    filename = models.CharField(max_length=100)
    image = models.ImageField(height_field=0, width_field=0)