from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from accounts.db import myclient

from accounts.apicall import get_response

# Create your views here.
@login_required
def view_progress(request):
    return render(request,'tracker/progress.html')
    # HttpResponse(request,<h1>hello</h1>)
    # return render(request,'tracker/progress.html')

# @login_required(login_url='login-page')
# def track_progress():
#     mydb = myclient["ClashofClans"]
#     mycol = mydb["accounts_customuser"]

#     # user_data = mycol.find_all({'playerTag': user_email})
#     user_data = mycol.find({'playerTag': {'$ne': ''}, })
#     print(len(user_data))

