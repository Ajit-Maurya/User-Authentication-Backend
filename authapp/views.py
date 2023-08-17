from django.shortcuts import render
from .models import UserAccount,UserLogInData
from .models import EmailValidationStatus
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request,'login.html',{'messege' : 'Only post method are allowed!'})
    email = request.POST.get('email')
    password = request.POST.get('password')
    hashed_password = make_password(password)
    if email is None and password is None:
        return render(request,'login.html',{'messege' : 'Please provide email and password'})
    try:
        registeredUser = get_object_or_404(UserLogInData,email_address = email, password_hash = hashed_password)
        emailStatus = EmailValidationStatus.objects.get(pk = registeredUser.email_validation_status)
        if emailStatus.email_validation_status == False:
            context = {
                'message' : 'Email is not varified. An email was sent to your email id with verification link, link will be only active for 10 minutes',
            }
            return render(request, 'verifications.html', context)
        context = {
            'username' : registeredUser.login_name,
        }
        return render(request, 'logged.html', context)
    except Exception as e:
        context = {
            'message' : 'user does not exists',
        }
        return render(request, 'login.html', context)

