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
        user = User.objects.get(id='123')
        Question.objects.create(
            question_text='question dummy',
            pub_date=timezone.now(), 
            poster=user
        )
        question = Question.objects.get(question_text='question dummy')
        Choice.objects.create(
            question=question,
            choice_text='right answer',
            correct=True)
        Choice.objects.create(
            question=question,
            choice_text='wrong answer',
            correct=False)
        Choice.objects.create(
            question=question,
            choice_text='wrong2 answer',
            correct=False)
        Choice.objects.create(
            question=question,
            choice_text='wrong3 answer',
            correct=False)

    def test_quiz(self):
        question = Question.objects.get(question_text='question dummy')
        c = question.choice_set.get(choice_text='right answer')
        self.assertEqual(c.correct, True)

        post_req = self.rf.post('/quiz/submit_quiz', {'question_text': question.question_text,
        'correct1': c, 'text1': c.choice_text})
        post_req.session = {'user': '1234'}
        views.submit_quiz(post_req)
        q = Question.objects.last()
        self.assertEqual(q.poster.id, '123')      
