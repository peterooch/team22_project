from django.test import TestCase
from .models import Post
from django.utils import timezone

class postTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            poster    = 'me',
            date      = timezone.now(),
            title     = 'test',
            content   = 'checking for test',
            forum_id  = 'milga'
        )

    def test_postDB_check(self):
        post = Post.objects.get(poster = 'me')
        self.assertEqual(post.title, 'test')
            