from django.urls import path
from . import views,signup,verify,edit

urlpatterns = [
    path('',views.home),
    path('login',views.login,name='login'),
    path('signup',signup.signup,name='signup'),
    path('home',views.homepage,name='home'),
    # path('externalProvider',views.externalProvider,name='externalProvider')
    path('verify',verify.verify,name='verify'),
    path('edit',edit.edit,name='edit'),
    path('confirm',edit.save_changes,name='save_changes')
    # path('home',home.home_page,name='home_page')
]