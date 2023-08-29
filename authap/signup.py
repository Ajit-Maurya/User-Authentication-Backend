from django.shortcuts import render,redirect
from .models import UserAccount,UserLogInData
from django.contrib.auth.hashers import make_password, check_password

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        hashed_password = make_password(request.POST.get('password'))
        user = UserAccount(first_name=first_name, last_name=last_name, gender=gender,dob=dob)
        user.save()
        userdata = UserLogInData(user_id=user,
                    password_hash=hashed_password,
                    email_address = email
                    )
        userdata.save()
        return render(request,'signup.html')
    return render(request,'signup.html')
