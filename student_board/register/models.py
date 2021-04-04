from django.db import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    first_name =  models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(User):
    department = models.TextField()
    approved = models.BooleanField(default=False)

class Faculty(User):
    courses = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)

    
