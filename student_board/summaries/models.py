from django.db import models
import os
from student_board import settings
# Create your models here.

class Documents(models.Model):
    location = models.TextField()
    user = models.CharField(max_length=10)
    title = models.TextField()
    course = models.TextField()
    file_size = models.TextField()
    additional = models.BooleanField(default=False)

    @property
    def relative_path(self):
        return os.path.relpath(self.location, settings.MEDIA_ROOT)


class Rules(models.Model):
    forum  = models.CharField(default='General', max_length=20)
    rules = models.TextField()

class Feedback(models.Model):
    DocumentID = models.ForeignKey(Documents, on_delete=models.CASCADE)
    feedback = models.TextField()


