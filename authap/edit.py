from django.shortcuts import render,redirect
import json
from .models import UserLogInData
from django.contrib.auth.hashers import check_password

def edit(request):
    token = request.session.get('token')
    if not token:
        return render(request,'login.html',{'message' : 'login before editing'})
    
    #deserialization
    context_json = request.session.get('context')
    context = json.loads(context_json)
    return render(request,'edit_page.html',context)

def save_changes(request):
    #error handling part
    if request.method != 'POST':
        return render(request,'error.html',{'message' : 'only post method are allowed'})
    token = request.session.get('token')
    if not token:
        return render(request,'login.html',{'message' : 'invalid request'})
    password = request.POST.get('password')
    print(token)
    if check_password(password,token) == False:
        return render(request,'edit_page.html',{'message' : 'wrong password'})
    
    #retrieving user data from database and through request
    user = UserLogInData.objects.get(confirmation_token=token)
    changed_user_data = request.POST.dict()

    user = user.user_id(first_name=changed_user_data['first_name'],
                        last_name=changed_user_data['last_name'],
                        gender = changed_user_data['gender'],
                        dob = changed_user_data['dob'])
    user.save()
    return render(request,'error.html',{'message' : 'edit were successful'})