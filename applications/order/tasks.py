from django.core.mail import send_mail
from jellyfish.celery import app

@app.task
def send_confirmation_code(email, code):
    full_link = f'Tap this -> http://34.159.20.148:80/api/v1/order/confirm/{code}'    
    send_mail(
        f'Order confirm',
        f'Please click link to confirm order:  {full_link}',
        'sabyrkulov.nurmuhammed@gmail.com',
        [email]
    )