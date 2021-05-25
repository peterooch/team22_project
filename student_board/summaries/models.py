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

    @property
    def relative_path(self):
        return os.path.relpath(self.location, settings.MEDIA_ROOT)


class Rules(models.Model):
    course = models.TextField()
    content = models.TextField()