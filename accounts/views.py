# from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from datetime import datetime
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from .apicall import get_response
from .db import myclient

# Create your views here.
mydb = myclient["COcDB"]
mycol = mydb["Users"]

@csrf_exempt
def update_player_data(request):
    print(request.method)
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            print(body)
            player_tag = body.get('tag')
            print(player_tag)
            if not player_tag:
                return JsonResponse({'error': 'Tag is required'}, status=400)

            # Replace this with your actual get_response function
            data = get_response(player_tag)

            # Normalize the JSON data
            normalized_all = pd.json_normalize(data)

            # Convert DataFrame to dictionary format suitable for MongoDB insertion
            records = normalized_all.to_dict(orient='records')

            # Add createdAt field with current timestamp
            created_at = datetime.utcnow()

            # Insert or update records in MongoDB collection
            for record in records:
                tag = record.get('tag')  # Assuming 'tag' is the field name for the primary key
                if tag:
                    record['createdAt'] = created_at
                    mycol.update_one({'tag': tag}, {'$set': record}, upsert=True)
                    print(f"Upserted document with tag {tag} into MongoDB.")
                else:
                    print(f"No 'tag' field found in the record: {record}")

            return JsonResponse({"message": f"Player data for tag {player_tag} processed successfully"})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt  
def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile-page')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for '+user)
            return redirect('login-page')  # Redirect to a different view after successful registration
    else:
        form = CreateUserForm()
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context)  # Ensure that the form is rendered

def registration_success(request):

    return render(request,'accounts/registration_success.html') 


@csrf_exempt  
def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app-home-page')  # Redirect to the core app home view
                # return redirect('profile-page')  # Redirect to a home page or another view after successful login
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Please fill out both fields')
    
    return render(request, 'accounts/login.html')

@login_required(login_url ='login-page')
def profile_view(request):
    return render(request,'accounts/profile.html')

def logout_view(request):
    logout(request)
    return redirect('login-page')

@login_required(login_url ='login-page')
def update_profile_view(request):
    return HttpResponse('<h1>Update Profile Here </h1>')

@login_required(login_url ='login-page')
def password_change_view(request):
    return HttpResponse('<h1>Password Change Here </h1>')

