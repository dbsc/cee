from django.db import models
from django.core import mail
from django.template import loader
from django.utils.html import strip_tags
class Email(models.Model):
    subject = models.CharField(
        max_length=250,
        help_text='The subejct of the email.'
    )
    message = models.TextField(
        blank=True,
        help_text='The text content of the email.'
    )
    sender = models.CharField(
        max_length=250,
        help_text="The sender address of the email."
    )
    receivers = models.JSONField(
        help_text="The receivers address of the email."
    )
    company = models.TextField(
        blank=True,
        null=True,
        help_text='The company that wants to send the email.'
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text='Basic content of the email.'
    )

    def send(self, data):
        subject = data.get('subject')
        message = data.get('message')
        sender = data.get('sender')
        receivers = data.get('receivers')
        company = data.get('company')
        description = data.get('description')
        html_message = loader.get_template('index.html').render({
            'company': company,
            'description': description
        })

        msg = mail.EmailMultiAlternatives(
            subject = subject,
            body = message,
            from_email = sender,
            to = [receivers]
        )

        msg.attach_alternative(html_message, "text/html")

        msg.send()
