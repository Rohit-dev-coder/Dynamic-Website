from django.shortcuts import render
from home.models import users
from django.http import HttpResponse

def dashboardpage(request):
    return render(request,'dashboard/dashboard.html')