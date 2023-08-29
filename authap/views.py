from django.shortcuts import render,redirect
from .models import UserAccount,UserLogInData
from .models import EmailValidationStatus,UserLoginDataExternal
from urllib.parse import urlencode
# from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password

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

        email_status = user.email_validation_status
        if not email_status.email_validation_status:
            context = {'message':'email is not verified'}
            return render(request, 'verification.html',context)
        context = {'token' : user.confirmation_token}
        return render(request,'logged.html',context)
    except UserAccount.DoesNotExist:
        context = {'message' : 'user does not exists',}
        return render(request, 'login.html', context)
    except EmailValidationStatus.DoesNotExist:
        context = {'message' : 'email is not registered'}
        return render(request, 'login.html',context)

def home(request):
    return render(request, 'login.html')


# def externalProvider(requset):
#     mock_auth_url = "https://github.com/login/oauth/authorize"
