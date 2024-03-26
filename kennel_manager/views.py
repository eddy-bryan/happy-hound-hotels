from django.shortcuts import render
from django.views import generic
from .models import Kennel

def home(request):
    return render(request, 'kennel_manager/index.html')


class KennelList(generic.ListView):
    queryset = Kennel.objects.all()
    template_name = 'kennel_list.html'


# def kennel_details():