from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Test")


# def search_results():


# def kennel_details():