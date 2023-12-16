from django.core.mail import send_mail
from urllib.parse import urlencode,urlparse,urlunparse
import secrets,string
import datetime

def create_url(token,base_url):
    encode_token = urlencode({'token':token})
    parse_url = urlparse(base_url)
    final_url = urlunparse(parse_url._replace(query=encode_token))
    return final_url

def mail(token,url,subject):
    base_url = "http://127.0.0.1:8000/" + url
    message = create_url(token,base_url)
    send_mail(
        subject,
        message,
        'django@mail.com',
        ['mauryaajit.am@gmail.com'],
        fail_silently=False,
    )

def generate_unique_string(length):
    characters = string.ascii_letters+string.digits

    random_string = ''.join(secrets.choice(characters) for _ in range(length))

    return random_string

def passwordRecoveryMail(userData):
    password_token = generate_unique_string(100) 
    token_generation_time = datetime.datetime.now()
    userData.password_recovery_token = password_token
    userData.recovery_token_time = token_generation_time
    userData.save()
    mail(password_token,"password-recovery","password recovery verification")

def valid_time_diff(time):
    given_time = str(time)
    given_time = given_time.split()
    curr_time = str(datetime.datetime.now())
    curr_time = curr_time.split()

    if(given_time[0] != curr_time[0]):
        return False
    if(given_time[1][0:2] != curr_time[1][0:2]):
        return False
    diff = int(curr_time[1][3:5]) - int(given_time[1][3:5])
    if(diff > 10):
        return False
    return True