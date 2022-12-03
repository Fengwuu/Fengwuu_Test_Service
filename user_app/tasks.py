from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



@shared_task
def send_reg_mail(email, username):
    message = render_to_string('email/hello_email.html', context={'username': username})
    user_mail = email
    email_subject = " Вы успешно прошли регистрацию! "
    email = EmailMessage(email_subject, message, to=[user_mail])
    email.send()  # Make email message to registered user


