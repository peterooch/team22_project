from django.db import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    first_name =  models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.TextField()


class Student(User):
    department = models.TextField()
    approved = models.BooleanField(default=False)

    
