from django.db import models

<<<<<<< Updated upstream
# Create your models here.

=======
#Name, ID, Courses, Email, Password, Approved
>>>>>>> Stashed changes
class User(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Id = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.TextField()

<<<<<<< Updated upstream
class Faculty(User):
    courses = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)
=======

class Faculty(User):
    courses = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)
>>>>>>> Stashed changes
