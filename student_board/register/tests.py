from django.test import TestCase
from .models import Student, Faculty, Admin
# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            id='1111',
            first_name='John',
            last_name='Doe',
            email='johndoe@localhost',
            password='1234',
            department='ABC')
        Faculty.objects.create(
            id='2222',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@localhost',
            password='1234',
            courses='ABCD'
        )
        Admin.objects.create(
            id='3333',
            first_name='Admin',
            last_name='Doe',
            email='admin@localhost',
            password='1234',
        )
    
    def test_1(self):
        student = Student.objects.get(id='1111')
        faculty = Faculty.objects.get(id='2222')
        admin   = Admin.objects.get(id='3333')

        self.assertEqual(str(student), 'John Doe')
        self.assertEqual(str(faculty), 'Jane Doe')
        self.assertEqual(str(admin), 'admin@localhost')
