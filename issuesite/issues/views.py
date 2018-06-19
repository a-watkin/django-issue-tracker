from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def issues(request):
    return HttpResponse("issues page")