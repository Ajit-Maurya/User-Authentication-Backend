from  django import forms
from .models import UserAccount

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['first_name','last_name','gender','dob','role_id']