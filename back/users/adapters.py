from django.utils.translation import gettext_lazy as _
from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError


class RestrictEmailAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        restricted_list = [
            'andredalbosco@gmail.com',
            'andredbsc@gmail.com',
        ]
        if email not in restricted_list:
            raise ValidationError(_('You are restricted from registering. Please contact admin.'))
        return email
