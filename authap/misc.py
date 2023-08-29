from django.core.mail import send_mail
from urllib.parse import urlencode,urlparse,urlunparse

def create_response(token):
    base_url = "https://127.0.0.1:8000/verify"
    encode_token = urlencode({'token':token})
    parse_url = urlparse(base_url)
    final_url = urlunparse(parse_url._replace(query=encode_token))
    return final_url

def mail(token):
    message = create_response(token)
    send_mail(
        'Account Verification',
        message,
        'django@mail.com',
        ['mauryaajit.am@gmail.com'],
        fail_silently=False,
    )
