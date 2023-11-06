from django.shortcuts import render
from .models import CustomUser,UserExtraLoginData
import datetime
from .misc import mail,generate_unique_string

def signup(request):
    if request.method == 'POST':
        #extrating necessary info from request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('password')

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
        )

        confirmation_token = generate_unique_string(100)    #this token will be used for validating email in signup
        token_generation_time = datetime.datetime.now()

        user_data = UserExtraLoginData(
                user = user,
                confirmation_token = confirmation_token,
                token_generation_time = token_generation_time
        )

        user_data.save()
        mail(confirmation_token,"verify","Account creation verification")
        return render(request,'error.html',{'message':'An email was sent to your email for account verification'})
    return render(request,'signup.html')
