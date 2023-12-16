# authentication.py
from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomUserAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id=None,email=None):
        try:
            if email is not None:
                return CustomUser.objects.get(email=email)
            else:
                return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
