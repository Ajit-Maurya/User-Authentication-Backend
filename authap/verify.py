from django.shortcuts import render
from .models import UserExtraLoginData
from .misc import generate_unique_string,mail,valid_time_diff
import datetime

def verify(request):
    token = request.GET.get('token')
    # if UserLogInData.objects.filter(confirmation_token=token).exists():
    try:
        user = UserExtraLoginData.objects.get(confirmation_token=token)
        if(valid_time_diff(user.token_generation_time)==False):
            confirmation_token = generate_unique_string(100)
            token_generation_time = datetime.datetime.now()
            mail(confirmation_token)
            user.token_generation_time = token_generation_time
            user.confirmation_token = confirmation_token
            user.save()
            return render(request,'error.html',{'message':'Earlier mail was expired, new mail has been sent'})
        else:
            user.email_validation_status = True
            user.save()
            return render(request,'error.html',{'message' : 'Your email is now verified, Login again'})
    except UserExtraLoginData.DoesNotExist:
        return render(request,'error.html',{'message':'invalid request, login again'})
    # else:
    #     return render(request,'error.html',{'message': 'Unauthorized'})