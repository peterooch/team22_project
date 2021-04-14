from django.db import models

# Create your models here.

class Documents(models.Model):
    location = models.TextField()
    user = models.CharField(max_length=10)
    title = models.TextField()
    course = models.TextField()