from django.shortcuts import render
from .models import UserAccount,UserLogInData
from django.contrib.auth.hashers import make_password, check_password
import secrets,string
import datetime
from django.core.mail import send_mail
from urllib.parse import urlencode,urlparse,urlunparse

def generate_unique_string(length):
    characters = string.ascii_letters+string.digits

    random_string = ''.join(secrets.choice(characters) for _ in range(length))

    return random_string

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

def signup(request):
    if request.method == 'POST':
        #extrating necessary info from request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        hashed_password = make_password(request.POST.get('password'))

        #creating user account
        user = UserAccount(first_name=first_name, last_name=last_name, gender=gender,dob=dob)
        user.save()

        #creating necessary info to stor userlogindata to create a relation
        confirmation_token = generate_unique_string(100)    #this token will be used for validating email in signup
        token_generation_time = datetime.datetime.now().time()
        userdata = UserLogInData(user_id=user,
                    password_hash=hashed_password,
                    email_address = email,
                    confirmation_token=confirmation_token,
                    token_generation_time=token_generation_time,
                    )
        userdata.save()
        #after creating user profile, Email will be sent to user for account verification
        mail(confirmation_token)
        return render(request,'error.html',{'message':'An email was sent to your email for account verification'})
    return render(request,'signup.html')
