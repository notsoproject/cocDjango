from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.apicall import get_response
from django.views.decorators.csrf import csrf_exempt
from .forms import ComparisonForm
import json



@login_required(login_url='login-page')
@csrf_exempt
def comparison_view(request):
    # Initialize context with form
    context = {
        'form': ComparisonForm(),
        'comparison': None  # This will hold comparison data if available
    }

    # Handle POST request when the form is submitted
    if request.method == 'POST':
        form = ComparisonForm(request.POST)
        if form.is_valid():
            id1 = form.cleaned_data['id1']
            id2 = form.cleaned_data['id2']

            # Assuming get_response is a function that fetches data based on id
            data1 = get_response(id1)
            data2 = get_response(id2)

            # Build comparison data
            comparison = [(key, data1.get(key), data2.get(key)) for key in set(data1.keys()) | set(data2.keys())]

            # Update context with new data
            context.update({
                'id1': data1,
                'id2': data2,
                'form': form,
                'comparison': comparison
            })

    # For GET requests or if the form is not valid, show the initial or updated form
    # Render everything to compare.html including results if available
    return render(request, 'comparisions/compare.html', context)