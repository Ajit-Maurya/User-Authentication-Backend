from django.shortcuts import render,redirect
from .models import UserExtraLoginData,CustomUser
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .misc import passwordRecoveryMail,valid_time_diff

# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        print(user)
        if user is not None:
            user_data = UserExtraLoginData.objects.get(user=user)
            if(user_data.email_validation_status):
                request.session['user_pk'] = user.pk
                login(request,user)
                return redirect('home')
            else:
                return render(request,'error.html',{'message':'Account is not verified, Please check your email!'})
        return render(request,'login.html',{'message':'Invaid username/password!'})
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
  
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def edit(request):
    return render(request,'edit_page.html')

@login_required
def saveChanges(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    gender = request.POST.get('gender')
    dob = request.POST.get('dob')
    pk = request.session.get('user_pk',None)
    userProfile = CustomUser.objects.get(pk=pk)

    print(first_name)
    userProfile.first_name = first_name
    userProfile.last_name = last_name
    userProfile.dob = dob
    userProfile.gender = gender

    userProfile.save()
    return render(request,'home.html')

def forgotPassword(request):
    return render(request,'password_recovery.html')

def passwordRecovery(request):
    email = request.POST.get('email')
    if email is None:
        email = request.session['email']
    password = request.POST.get('password')
    try:
        user = CustomUser.objects.get(email=email)
        request.session['email'] = email
    except CustomUser.DoesNotExist:
        user = None
    if user is not None and password is None:
        userData = UserExtraLoginData.objects.get(user=user)
        if userData.password_recovery_token == None or valid_time_diff(userData.recovery_token_time) == False:
            passwordRecoveryMail(userData)
            return render(request,'error.html',{'message' : 'An email was sent to your email address for password recovery'})
        else:
            return render(request,'password_change.html')
    elif user is not None and password is not None:
        user.set_password(password)
        user.save()
        request.session['email'] = None
        return render(request,'error.html',{'message':'your password has been set. Login again!'})
    else:
        return render(request,'error.html',{'message':'no such user exist!'})