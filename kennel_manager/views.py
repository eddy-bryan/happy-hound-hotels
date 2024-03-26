from django.shortcuts import render
from django.views import generic
from .models import Kennel
# Remove HttpReponse after replacing home view
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Kennel manager")


class KennelList(generic.ListView):
    queryset = Kennel.objects.all()
    template_name = 'kennel_list.html'


# def kennel_details():