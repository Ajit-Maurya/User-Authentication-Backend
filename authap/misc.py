from django.core.mail import send_mail
from urllib.parse import urlencode,urlparse,urlunparse
import secrets,string
from datetime import datetime

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

def generate_unique_string(length):
    characters = string.ascii_letters+string.digits

    random_string = ''.join(secrets.choice(characters) for _ in range(length))

    return random_string

def valid_confirmation_token(time):
    curr_time = datetime.now().time()
    time_difference = datetime.combine(datetime.min,curr_time) - datetime.combine(datetime.min,time)
    minutes_difference = time_difference.total_seconds()/60
    if minutes_difference > 1:
        return False
    return True
