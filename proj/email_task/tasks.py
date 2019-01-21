# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import smtplib
import requests


@shared_task
def mass_send(msg_id, msg_from, msg_to, subject, text_content, html_content):
    try:
        msg = EmailMultiAlternatives(
            subject, text_content, msg_from, [msg_to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except smtplib.SMTPException:
        return 'Email not sent'
    return msg_id


# add.apply_async((7,30), link=on_success.s())
@shared_task
def email_on_success(msg_id):
    print("The msg ID: ", msg_id)
    domain = settings.CALLBACK_DOMAIN
    url = '{}/api/management/email_task_callback/{}/'.format(domain, msg_id)
    try:
        requests.post(url, data={'token': settings.CELERY_API_KEY})
    except requests.exceptions.Timeout:
        return "Timeout"
    except requests.exceptions.HTTPError:
        return "HTTP Error"
    except requests.exceptions.ConnectionError:
        return "Connection Error"
    return "Successfully Acknowledged"
