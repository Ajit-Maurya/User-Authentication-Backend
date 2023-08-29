from django.urls import path
from . import views,signup,verify

urlpatterns = [
    path('',views.home),
    path('login',views.login,name='login'),
    path('signup',signup.signup,name='signup'),
    # path('externalProvider',views.externalProvider,name='externalProvider')
    path('verify',verify.verify,name='verify'),
]