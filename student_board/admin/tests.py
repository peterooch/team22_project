from django.db.models import Model
from django.test import TestCase
from .models import AdminAlert, Rules
from django.test.client import RequestFactory  
from register.models import Faculty, Student, User
from summaries.models import Documents
from . import views
# Create your tests here.

class rulesTest(TestCase):
    def setUp(self):
        Rules.objects.create(forum='Jobs', rules='rules')

    def test_doc(self):
        ru = Rules.objects.get(forum='Jobs')
        self.assertEqual(ru.rules, 'rules')        

# Test the various alert functions   
class alertTests(TestCase):
    def setUp(self) -> None:
        self.rf = RequestFactory()
        self.dummy_user = User.objects.create(
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
    # Test alert creation
    def test_createalert(self):
        post_req = self.rf.post('/admin/createalert', {'doc_id': self.dummy_doc.id, 'info': 'dummy alert'})
        post_req.session = {'user': '1234'}
        views.createalert(post_req)
        alert = AdminAlert.objects.last()

        self.assertEqual(alert.document.id, self.dummy_doc.id)
        self.assertEqual(alert.reporter.id, '1234')
    # Test alert deletion without document deletion
    def test_deletealert(self):
        alert = AdminAlert.objects.create(
            reporter = self.dummy_user,
            document = self.dummy_doc,
            info = 'dummy alert'
        )
        alert_id = alert.id
        views.deletealert(None, alert_id)

        self.assertFalse(AdminAlert.objects.filter(id=alert_id).exists())
    # Test alert deletion with deleting relevant document
    def test_handlealert(self):
        alert = AdminAlert.objects.create(
            reporter = self.dummy_user,
            document = self.dummy_doc,
            info = 'dummy alert'
        )
        alert_id = alert.id
        doc_id = self.dummy_doc.id
        views.handlealert(None, alert_id)
        
        self.assertFalse(AdminAlert.objects.filter(id=alert_id).exists())
        self.assertFalse(Documents.objects.filter(id=doc_id).exists())

class userMgmtTests(TestCase):
    def setUp(self) -> None:
        self.rf = RequestFactory()
        Student.objects.create(
            id='123456',
            first_name='dummy',
            last_name='dummy',
            email='dummy2@dummy.com',
            password='dummy',
            department='SW Eng' 
        )
    def test_approve(self):
        views.approve(None, '123456')

        self.assertTrue(Student.objects.get(id='123456').approved)
    def test_student_to_faculty(self):
        get_req = self.rf.get('/admin/convert/123456')
        views.student_to_faculty(get_req, '123456')

        self.assertFalse(Student.objects.filter(id='123456').exists())
        self.assertTrue(Faculty.objects.filter(id='123456').exists())
    def test_deleteuser(self):
        views.deleteuser(None, '123456')

        self.assertFalse(Faculty.objects.filter(id='123456').exists())
