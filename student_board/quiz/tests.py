from django.test import TestCase
from quiz.models import Question,Choice
from register.models import User
from django.utils import timezone
from django.test.client import RequestFactory
from quiz import views

class quiz_test(TestCase):
    def setUp(self):
        self.rf = RequestFactory()
        User.objects.create(
            id='123',
            first_name='dummy',
            last_name='dummy',
            email='dummy@mail.com',
            password='dummy'
        )
        self.user = User.objects.get(id='123')
        Question.objects.create(
            question_text='question dummy',
            pub_date=timezone.now(), 
            poster=self.user
        )
        self.question = Question.objects.get(question_text='question dummy')
        Choice.objects.create(
            question=self.question,
            choice_text='right answer',
            correct=True)
        Choice.objects.create(
            question=self.question,
            choice_text='wrong answer',
            correct=False)
        Choice.objects.create(
            question=self.question,
            choice_text='wrong2 answer',
            correct=False)
        Choice.objects.create(
            question=self.question,
            choice_text='wrong3 answer',
            correct=False)

    def test_quiz(self):
        self.c = self.question.choice_set.get(choice_text='right answer')
        self.assertEqual(self.c.correct, True)
        self.c2 = self.question.choice_set.get(choice_text='wrong answer')
        post_req = self.rf.post('/quiz/submit_quiz', {'question_text': self.question.question_text,
        'choice_text1': self.c.choice_text,'choice_text2': self.c2.choice_text,
        'choice_text3': self.c2.choice_text,'choice_text4': self.c2.choice_text})
        post_req.session = {'user': '123'}
        views.submit_quiz(post_req)
        q = Question.objects.last()
        self.assertEqual(q.poster, 'dummy')      
