import requests
from dotenv import load_dotenv
import os
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AlbumSerializer
from .models import Album

# Create your views here.

class AlbumView(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

def search_disco(request):
    load_dotenv('/Users/williamhbelew/Hacking/vinyl/backend/.env')
    user_token = os.getenv('USER_TOKEN')
    r = requests.get('https://api.discogs.com/database/search?q=The+Beatles&token=' + user_token)
    return HttpResponse(r)