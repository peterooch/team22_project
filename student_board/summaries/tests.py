from django.test import TestCase
from .models import Documents
from student_board import settings
from django.test.client import RequestFactory  
from register.models import Faculty, Student, User
from django.core.files.storage import FileSystemStorage
from . import views
from django.core.files.uploadedfile import SimpleUploadedFile



# Create your tests here.
class docTest(TestCase):
    def setUp(self) -> None:
        self.rf = RequestFactory()
        self.dummy = Documents.objects.create(
            location = settings.MEDIA_ROOT,
            user = "123456789",
            title ='doc',
            course = 'course',
            file_size = 0
            )
        self.file = SimpleUploadedFile(
            "doc",
            b"doc"
        )

    def test_doc(self):
        doc = Documents.objects.get(title="doc")
        self.assertEqual(doc.user, '123456789')
    
    def test_createSum(self):
        post_req = self.rf.post('/summaries/submit', {
            'file' : self.file,
            'location': self.dummy.location,
            'title': self.dummy.title,
            'user':self.dummy.user,
            'course':self.dummy.course,
            'file_size':self.dummy.file_size,
            'additional': 'additional'})
        post_req.session = {'user': '1234'}
        views.submitSum(post_req)
        doc = Documents.objects.last()

        self.assertEqual(doc.title, self.dummy.title)
