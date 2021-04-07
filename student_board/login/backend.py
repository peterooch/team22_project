from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.apps import apps
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, email=None):
        UserModel = apps.get_model('register', 'User')
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        
        #if check_password(password,user.password):
        if password==user.password:
            return user

        return None