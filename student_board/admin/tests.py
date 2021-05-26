from django.test import TestCase
from .models import Rules

# Create your tests here.

class rulesTest(TestCase):
    def setUp(self):
        Rules.objects.create(forum='Jobs', rules='rules')

    def test_doc(self):
        ru = Rules.objects.get(forum='Jobs')
        self.assertEqual(ru.rules, 'rules')        
        