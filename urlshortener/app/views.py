from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners

# Create your views here.

def index(request):
    # original_url = request.POST['url']
    

    # urlshortener = pyshorteners.Shortener()
    # urlshorted = urlshortener.tinyurl.short(original_url)

    # context = {
    #     'original_url': original_url,
    #     'urlshorted': urlshorted
    # }
    
    return render(request, 'app/template/index.html')


def shorted(request):
    url = request.POST['url']

    shortener = pyshorteners.Shortener()
    url_shorted = shortener.tinyurl.short(url)

    context = {
        'original_url': url,
        'url_shorted': url_shorted,
    }
    return render(request, 'app/template/shorted.html', context)


