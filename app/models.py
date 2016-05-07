from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class User(models.Model):
    name = models.charField(max_length=200)



class Photo(models.Model):
    user = models.ForeignKey(User, unique=True)
    profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)

class Task(models.Model):
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
