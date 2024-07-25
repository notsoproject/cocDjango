# from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.http import HttpResponse, JsonResponse
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # replace with your success URL
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def registration_success(request):
    return render(request,'accounts/registration_success.html') 

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

