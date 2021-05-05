from django.test import TestCase
from .models import Documents
from student_board import settings


# Create your tests here.
class docTest(TestCase):
    def setUp(self):
        Documents.objects.create(location=settings.MEDIA_ROOT, user="123456789", title='doc', course='db', file_size=0)

    def test_doc(self):
        doc = Documents.objects.get(title="doc")
        self.assertEqual(doc.user, '123456789')
        