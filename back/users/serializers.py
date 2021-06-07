from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.conf import settings


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        fields = ['pk']
        read_only_fields = ['email']


class CustomLoginSerializer(LoginSerializer):
    username = None

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = self.get_auth_user(email, password)

        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise ValidationError(msg)

        self.validate_auth_user_status(user)

        if 'dj_rest_auth.registration' in settings.INSTALLED_APPS:
            self.validate_email_verification_status(user)

        attrs['user'] = user
        return attrs

    def get_auth_user(self, email, password):
        return super().get_auth_user(None, email, password)


class CustomRegisterSerializer(RegisterSerializer):
    username = None

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email'),
            'password1': self.validated_data.get('password1')
        }
