

import requests
from django.shortcuts import render
from .api_keys import NETDETECTIVE_API_KEY
# from django.contrib.auth import authenticate, login


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


def query(request):
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

        return render(request, 'api/query.html', {'result': result})

    return render(request, 'api/query.html', {'result': None})


# def app_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page or perform other actions
#             return redirect('home')  # Redirect to the home page
#         else:
#             # Handle invalid login
#             return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
#     else:
#         return render(request, 'registration/login.html')
