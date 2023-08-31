from django.urls import path
from . import views,signup,verify,edit
from . import home

urlpatterns = [
    path('',views.home),
    path('login',views.login,name='login'),
    path('signup',signup.signup,name='signup'),
    # path('externalProvider',views.externalProvider,name='externalProvider')
    path('verify',verify.verify,name='verify'),
    path('edit',edit.edit,name='edit'),
    path('home',home.home_page,name='home_page')
]