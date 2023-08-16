from django.shortcuts import render
from .models import UserAccount,UserLogInData
from .models import EmailValidationStatus
from django.shortcuts import get_list_or_404

# Create your views here.
def login(request):
    try:
        registeredUser = get_list_or_404(UserLogInData, user_id = request.user.id)
        emailStatus = EmailValidationStatus.objects.get(pk = registeredUser.email_validation_status)
        if emailStatus.email_validation_status == False:
            context = {
                'message' : 'Email is not varified. An email was sent to your email id with verification link, link will be only active for 10 minutes',
            }
            return render(request, 'login_failed.html', context)
        context = {
            'username' : registeredUser.login_name,
        }
        return render(request, 'logged.html', context)
    except Exception as e:
        return render(request, 'Login_failed.html')