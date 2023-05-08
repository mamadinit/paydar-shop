from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .exceptions import UserNotVerified
from django.contrib import messages

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = User.objects.get(phone=username)
        except User.DoesNotExist:
            print('User.DoesNotExist')
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                if self.user_is_verified(user):
                    return user
                else:
                    request.session['phone'] = user.phone
                    request.session.set_expiry(300)
                    messages.error(request, 'ابتدا شماره موبایل خود را تایید کنید', 'info')
                    raise UserNotVerified('')

    def user_is_verified(self, user):
        is_verified = getattr(user, 'is_verified', None)
        return is_verified or is_verified is None 