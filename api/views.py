import requests
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .api_keys import NETDETECTIVE_API_KEY
from .models import Profile, Query
from .forms import SignUpForm


# IndexPage
def index(request):
    try:
        url = "https://netdetective.p.rapidapi.com/query"
        headers = {
            "X-RapidAPI-Key": NETDETECTIVE_API_KEY,
            "X-RapidAPI-Host": "netdetective.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            retrieved_data = response.json()['result']
        else:
            retrieved_data = {}

    except Exception as e:
        # Log the exception to see what went wrong
        print(f"Error occurred: {e}")
        retrieved_data = {}
    return render(request, 'api/index.html', {'data': retrieved_data})


@login_required()
# Custom IP Query Page
def query(request):
    result = None  # Initialize result variable
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')

        try:
            url = "https://netdetective.p.rapidapi.com/query"
            headers = {
                "X-RapidAPI-Key": NETDETECTIVE_API_KEY,
                "X-RapidAPI-Host": "netdetective.p.rapidapi.com"
            }
            params = {
                "ipaddress": ip_address  # Pass the entered IP address to the API
            }

            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                result = response.json()['result']
                query = Query.objects.create(user=request.user, ip_address=ip_address)
            else:
                # Handle API request failure
                result = None

        except requests.RequestException as e:
            # Handle request exceptions (e.g., connection error, timeout)
            print(f"Request Exception: {e}")
            result = None
        except Exception as ex:
            # Handle other exceptions
            print(f"An error occurred: {ex}")
            result = None
    queries = Query.objects.filter(user=request.user)
    return render(request, 'api/query.html', {'result': result, 'queries': queries})


# Profile Page
@login_required
def profile_view(request):
    user = request.user
    try:
        user_profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        user_profile = None

    context = {
        'user': user,
        'user_profile': user_profile,
    }

    return render(request, 'api/profile.html', context)


def logout(request):
    django_logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('index')  # Redirect to the index page after logout


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page, login page, or any desired URL after sign-up
            return redirect('login')  # Redirect to the login page after successful sign-up
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})