from django.shortcuts import render
from django.http import HttpResponse

def index(requsest):
    return HttpResponse("Hello,World!")

# Create your views here.
