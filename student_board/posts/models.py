from django.db import models

# Create your models here.

class Post(models.Model):
    poster    = models.CharField('Poster', max_length=10)
    date      = models.DateTimeField('Date Posted')
    title     = models.TextField('Post Title')
    content   = models.TextField('Post Content')
    forum_id  = models.CharField('Forum', default='General', max_length=20)

    def __str__(self):
        return self.title
