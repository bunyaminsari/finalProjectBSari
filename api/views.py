import requests
from django.shortcuts import render
from .api_keys import NETDETECTIVE_API_KEY

def index(request):
    # Implement logic to send queries to the NetDetective API
    # Use NETDETECTIVE_API_KEY in the headers of your API requests
    # Handle the response data accordingly
    # Render the index page with the retrieved data

    url = "https://netdetective.p.rapidapi.com/query"
    headers = {
        "X-RapidAPI-Key": NETDETECTIVE_API_KEY,
        "X-RapidAPI-Host": "netdetective.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    retrieved_data = response.json()
    return render(request, 'index.html', {'data': retrieved_data})


