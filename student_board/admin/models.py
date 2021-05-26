from django.db import models

# Create your models here.

class Rules(models.Model):
    forum  = models.CharField(default='General', max_length=20)
    rules = models.TextField()