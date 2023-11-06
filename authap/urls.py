from django.urls import path
from . import views,signup,verify,edit

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.loginUser,name='login'),
    path('signup',signup.signup,name='signup'),
    path('verify',verify.verify,name='verify'),
    path('edit',views.edit,name='edit'),
    path('confirm',views.saveChanges,name='save_changes'),
    path('logout',views.logout_view,name='logout'),
    path('forgot-password',views.forgotPassword,name='forgot_password'),
    path('password-recovery',views.passwordRecovery,name='password_recovery'),
]