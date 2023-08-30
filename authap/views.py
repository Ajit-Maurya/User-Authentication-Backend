from django.shortcuts import render
from .models import UserAccount,UserLogInData
from django.contrib.auth.hashers import make_password, check_password
from .misc import generate_unique_string,mail, valid_confirmation_token
from datetime import datetime

# Create your views here.

def login(request):
    if request.method != 'POST':
        return render(request,'login.html',{'message' : 'Only post method are allowed!'})
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if email is None or password is None:
        return render(request,'login.html',{'message' : 'Please provide email and password'})
    
    hashed_password = make_password(password) 
    try:
        user = UserLogInData.objects.get(email_address=email)
        if not check_password(hashed_password,user.password_hash):
            raise UserLogInData.DoesNotExist
        
        #handling the case where email was not verified
        if not user.email_validation_status:
            if not valid_confirmation_token(user.token_generation_time):
                context = {'message':'email is not verified,check your email'}
                return render(request, 'error.html',context)
            else:
                user.confirmation_token = generate_unique_string(100)
                user.token_generation_time = datetime.now().time()
                user.save()
                mail(user.confirmation_token)
                return render(request,'error.html',{'message':'An email was sent to your email for account verification'})
        
        #if user exits and verified
        context = {'token' : user.confirmation_token}
        return render(request,'home.html',context)
    
    #wrong password or invalid user
    except UserAccount.DoesNotExist:
        context = {'message' : 'Invalid user or Wrong password',}
        return render(request, 'login.html', context)

def home(request):
    return render(request, 'login.html')


# def externalProvider(requset):
#     mock_auth_url = "https://github.com/login/oauth/authorize"
