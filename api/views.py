import requests
from django.shortcuts import render
from .api_keys import NETDETECTIVE_API_KEY

def index(request):
    url = "https://netdetective.p.rapidapi.com/query"
    headers = {
        "X-RapidAPI-Key": NETDETECTIVE_API_KEY,
        "X-RapidAPI-Host": "netdetective.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        retrieved_data = response.json()['result']
    else:
        # Handle API request failure or errors here
        retrieved_data = {}
    print(retrieved_data)
    return render(request, 'index.html', {'data': retrieved_data})

def detail(request, item_id):
    url = "https://netdetective.p.rapidapi.com/query"
    headers = {
        "X-RapidAPI-Key": NETDETECTIVE_API_KEY,
        "X-RapidAPI-Host": "netdetective.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        retrieved_data = response.json()['result']
    else:
        # Handle API request failure or errors here
        retrieved_data = []

    # Find the specific item using its ID
    item = next((item for item in retrieved_data if item.get('id') == item_id), None)

    if not item:
        # If the item with the specified ID is not found, return a 404 page or handle accordingly
        return render(request, '404.html')

    return render(request, 'details.html', {'item': item})
