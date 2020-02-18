from django.shortcuts import render
import json
import requests



def home(request):
    # Grab some Price Data
    price_request =  requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,LTC,USDT,EOS,BNB,HMR,TRX,ETC,NEO,MIOTA&tsyms=USD')
    price = json.loads(price_request.content)


    # Grab some crypto news
    api_request =  requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api':api, 'price': price })

def prices(request):
    if request.method == 'POST':
        #quote = request.POST.get('quote', 'none')
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request =  requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote':quote, 'crypto': crypto})
    else:
        notfound = ' Enter a proper crypto symbol that mathes real cryptocurrency'
        return render(request, 'prices.html', {'notfound': notfound })


 
