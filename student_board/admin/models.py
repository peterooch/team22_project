from django.db import models
from register.models import User
from summaries.models import Documents
# Create your models here.

class Rules(models.Model):
    forum  = models.CharField(default='General', max_length=20)
    rules = models.TextField()

class AdminAlert(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    info     = models.TextField()
