from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def register_view(request):
    return HttpResponse('<h1>Register Here </h1>')

def login_view(request):
    return HttpResponse('<h1>Login Here </h1>')

def profile_view(request):
    return HttpResponse('<h1>Profile Here </h1>')

def logout_view(request):
    return HttpResponse('<h1>Logout Here </h1>')

def update_profile_view(request):
    return HttpResponse('<h1>Update Profile Here </h1>')

def password_change_view(request):
    return HttpResponse('<h1>Password Change Here </h1>')

