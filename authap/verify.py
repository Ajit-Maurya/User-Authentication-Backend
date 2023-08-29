from django.shortcuts import render
from .models import UserLogInData


def verify(request):
    token = request.GET.get('token')
    # if UserLogInData.objects.filter(confirmation_token=token).exists():
    try:
        user = UserLogInData.objects.get(confirmation_token=token)
        user.email_validation_status = True
        user.save()
        return render(request,'error.html',{'message' : 'Your email is now verified, Login again'})
    except UserLogInData.DoesNotExist:
        return render(request,'error.html',{'message':'invalid request'})
    # else:
    #     return render(request,'error.html',{'message': 'Unauthorized'})