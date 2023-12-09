import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .api_keys import NETDETECTIVE_API_KEY
from .models import Profile, Query
from .forms import SignUpForm


# IndexPage
def index(request):
    retrieved_data = {}
    # Check if the user is authenticated & If the user is already logged in the message will be displayed once.
    if request.user.is_authenticated and not request.session.get('has_seen_welcome_message', False):
        messages.info(request, request.user.username + ", you have just signed in!")
        request.session['has_seen_welcome_message'] = True

    # The success message is displayed once.
    if not request.session.get('has_seen_api_message', False):
        try:
            url = "https://netdetective.p.rapidapi.com/query"
            headers = {
                "X-RapidAPI-Key": NETDETECTIVE_API_KEY,
                "X-RapidAPI-Host": "netdetective.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                messages.success(request, "Data successfully retrieved from the API.")
                request.session['has_seen_api_success_message'] = True
                retrieved_data = response.json().get('result', {})
            else:
                retrieved_data = {}

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                messages.error(request, "Unauthorized access. Please check your API key.")
            else:
                messages.warning(request, f"API Error: {e}")
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
    last_five_queries = Query.objects.all().order_by('-id')[:5][::-1]
    return render(request, 'api/query.html', {'result': result, 'queries': last_five_queries})


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
