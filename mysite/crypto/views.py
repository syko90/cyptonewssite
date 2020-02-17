from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    api_request =  requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api':api })