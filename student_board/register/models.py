from django.db import models

class User(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Id = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.TextField()


class Student(User):
    department = models.TextField()
    approved = models.BooleanField(default=False)

class Faculty(User):
    courses = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)

    
