from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url ='login-page')
def home_view(request):
    # return HttpResponse("Welcome to the Clash of Clans Data Tracker!")
    return render(request,'core/home.html')

def about_view(request):
    return render(request,'core/about.html')


def contact_view(request):
    return render(request,'core/contact.html')

def error_404_view(request, exception):
    return HttpResponse("404 - Page not found", status=404)

def error_500_view(request):
    return HttpResponse("500 - Server error", status=500)