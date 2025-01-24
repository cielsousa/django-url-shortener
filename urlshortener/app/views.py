from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from datetime import datetime
import pyshorteners

from rest_framework import serializers, viewsets

from .models import Url


# Create your views here.


# API Views
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'is_active']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Url
        fields = ['date_shorten', 'url_original', 'url_shorted', 'number_visits']


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer



# URL Shortener views
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
    url_shorten = request.POST['url']

    shortener = pyshorteners.Shortener()
    url_shorted = shortener.tinyurl.short(url_shorten)

    url_instance = Url(
                       url_original=url_shorten,
                       url_shorted = url_shorted,
                       number_visits = 0)
    
    url_instance.save()

    context = {
        'original_url': url_shorten,
        'url_shorted': url_shorted,
    }
    return render(request, 'app/template/shorted.html', context)


