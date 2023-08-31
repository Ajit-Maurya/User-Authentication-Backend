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
    
    try:
        user = UserLogInData.objects.get(email_address=email)
        if check_password(password,user.password_hash) == False:
            context = {'message': 'Invalid user or Wrong password'}
            return render(request, 'login.html', context)
        
        #handling the case where email was not verified
        if not user.email_validation_status:
            if valid_confirmation_token(user.token_generation_time):
                context = {'message':'email is not verified,check your email'}
                return render(request, 'error.html',context)
            else:
                user.confirmation_token = generate_unique_string(100)
                user.token_generation_time = datetime.now().time()
                user.save()
                mail(user.confirmation_token)
                return render(request,'error.html',{'message':'An email was sent to your email for account verification'})
        
        #if user exits and verified
        user_info = user.user_id
        context = {
            'email' : user.email_address,
            'token' : user.confirmation_token,
            'first_name' : user_info.first_name,
            'last_name' : user_info.last_name,
            'gender' : user_info.gender,
            'dob' : user_info.dob
                }
        return render(request,'home.html',context)
    
    #wrong password or invalid user
    except UserLogInData.DoesNotExist or UserAccount.DoesNotExist:
        context = {'message' : 'Invalid user or Wrong password',}
        return render(request, 'login.html', context)

def home(request):
    return render(request, 'login.html')


# def externalProvider(requset):
#     mock_auth_url = "https://github.com/login/oauth/authorize"
