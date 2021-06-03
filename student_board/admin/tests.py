from django.test import TestCase
from .models import AdminAlert, Rules
from django.test.client import RequestFactory  
from register.models import User
from summaries.models import Documents
from . import views
# Create your tests here.

class rulesTest(TestCase):
    def setUp(self):
        Rules.objects.create(forum='Jobs', rules='rules')

    def test_doc(self):
        ru = Rules.objects.get(forum='Jobs')
        self.assertEqual(ru.rules, 'rules')        
        
class alertTests(TestCase):
    def setUp(self) -> None:
        self.rf = RequestFactory()
        User.objects.create(
            id='1234',
            first_name='dummy',
            last_name='dummy',
            email='dummy@dummy.com',
            password='dummy'
        )
        self.dummy_doc = Documents.objects.create(
            location='dummy.txt',
            user='1234',
            title='dummy.txt',
            course='dummy',
            file_size='1000',
        )
    def test_createalert(self):
        post_req = self.rf.post('/admin/createalert', {'doc_id': self.dummy_doc.id, 'info': 'dummy alert'})
        post_req.session = {'user': '1234'}
        views.createalert(post_req)
        alert = AdminAlert.objects.last()

        self.assertEqual(alert.document.id, self.dummy_doc.id)
        self.assertEqual(alert.reporter.id, '1234')
        