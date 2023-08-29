from django.shortcuts import render
from .models import UserLogInData


def verify(request):
    confirmation_token = request.GET.get('token')
    if UserLogInData.objects.filter(confirmation_token=confirmation_token).exists():
        user = UserLogInData.objects.get(confirmation_token=confirmation_token)
        user.email_validation_status = True
        user.save()
        return render(request,'error.html',{'message' : 'Your email is now verified, Login again'})
    else:
        return render(request,'error.html',{'message': 'Unauthorized'})