from django.urls import path

from . import views
urlpatterns = [
path('Registerpage/',views.registerPageView,name="register"),
path('loginpage/',views.loginView,name="login"),
path('loginprocess/',views.loginprocess,name="loginprocess"),
path('signup/',views.register,name="signup"),
path('', views.homePageView, name ='index'),
]
