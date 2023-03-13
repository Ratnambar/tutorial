from time import sleep
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_feedback_email_task(email_address, message):
    sleep(20)
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank You !",
        "guptaratnambar123@gmail.com",
        ["ratnambar123gupta@gmail.com"],
        fail_silently=False
    )