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
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
mydb = myclient["ClashofClans"]
mycol = mydb["accounts_users_details"]

# @login_required(login_url ='login-page')
@csrf_exempt
def update_player_data(player_tag):
    try:
        print(player_tag)
        # Replace this with your actual get_response function
        data = get_response(player_tag)
        print(data)

        # Normalize the JSON data
        normalized_all = pd.json_normalize(data)

        # Convert DataFrame to dictionary format suitable for MongoDB insertion
        records = normalized_all.to_dict(orient='records')

        # Add createdAt field with current timestamp
        updated_at = datetime.utcnow()

        # Insert or update records in MongoDB collection
        for record in records:
            tag = record.get('tag')
            # if tag:
            record['createdAt'] = updated_at
            mycol.update_one({'tag': tag}, {'$set': record}, upsert=True)
            print(f"Upserted document with tag {tag} into MongoDB.")
            # else:
            #     print(f"No 'tag' field found in the record: {record}")

        return True, f"Player data for tag {player_tag} processed successfully"
    except Exception as e:
        return False, str(e)

@csrf_exempt  
def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile-page')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            player_tag = form.cleaned_data.get('playerTag')  # Assuming you've added a player_tag field to your form
            
            # Call update_player_data
            success, message = update_player_data(player_tag)
            
            if success:
                messages.success(request, f'Account created successfully for {email}. {message}')
            else:
                messages.warning(request, f'Account created, but there was an issue updating player data: {message}')
            
            return redirect('login-page')
    else:
        form = CreateUserForm()
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def registration_success(request):

    return render(request,'accounts/registration_success.html') 


@csrf_exempt  
def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile-page')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email and password:
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                player_tag = user.playerTag
                print(f"User's player tag: {player_tag}")
                # Call update_player_data
                success, message = update_player_data(player_tag)
                print(success)
                login(request, user)
                messages.success(request,'Login Successful')
                return redirect('app-home-page')  # Redirect to the core app home view
                # return redirect('profile-page')  # Redirect to a home page or another view after successful login
            else:
                messages.error(request, 'Invalid email or password')
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

