from django.shortcuts import render,redirect
from .models import UserAccount,UserLogInData
from django.contrib.auth.hashers import make_password, check_password
from .misc import generate_unique_string,mail, valid_confirmation_token
from datetime import datetime
import json

# Create your views here.

def login(request):
    #checks if user is already logged in or not
    token = request.session.get('token')
    if token:
        return secure_login(request)
    
    if request.method != 'POST':
        return render(request,'login.html',{'message' : 'Only post method are allowed!'})
    
    #email and password verification
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
        
        request.session['token'] = user.confirmation_token
        return secure_login(request)
    
    #wrong password or invalid user
    except UserLogInData.DoesNotExist or UserAccount.DoesNotExist:
        context = {'message' : 'Invalid user or Wrong password',}
        return render(request, 'login.html', context)

def home(request):
    return render(request, 'login.html')

def secure_login(request):
    token = request.session.get('token')
    if not token:
        return render(request,'error.html',{'message' : 'Authentication token not found. Please log in.'})
    #for already logged in user
    context_json = request.session.get('context')
    if context_json:
        #deserialization of json to dict
        context = json.loads(context_json)
        return render(request,'home.html',context)
    
    user  = UserLogInData.objects.get(confirmation_token=token)
    user_info = user.user_id
    context = {
        'first_name' : user_info.first_name,
        'last_name' : user_info.last_name,
        'gender' : user_info.gender,
        'dob' : user_info.dob.strftime('%Y-%m-%d'),
        'email' : user.email_address,
        'token' : user.confirmation_token,
    }
    # serialization of data - dict to json
    context_json = json.dumps(context)
    request.session['context'] = context_json
    return render(request,'home.html',context)

# def externalProvider(requset):
#     mock_auth_url = "https://github.com/login/oauth/authorize"
