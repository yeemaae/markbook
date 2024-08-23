from django.contrib.auth.models import User
from .models import Profile


def create_profile(backend, user, *args, **kwargs):
    """Creating Profile with social auth"""
    Profile.objects.get_or_create(user=user)


class EmailAuthBackend:
    """
    Authentication with Email
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
