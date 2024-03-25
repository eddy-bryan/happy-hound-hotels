from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Kennel manager")


# def search_results():


# def kennel_details():