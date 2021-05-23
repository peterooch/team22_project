from django.db import models
from django.db.models.enums import Choices

class Question(models.Model):
    question_text = models.CharField('question text', max_length=200)
    pub_date = models.DateTimeField('published date')
    poster = models.CharField(max_length=50)
    
    def __str__(self):
        return self.question_text
    
    def get_ans(self):
        return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.choice_text + " | " + str(self.correct)