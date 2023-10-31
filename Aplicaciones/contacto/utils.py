from django.core.mail import send_mail
from django.conf import settings


def send_email_test():    
    subject="Correo Prueba",
    message='Nos comunicamos contigo',
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=["projecthouse2120@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)
