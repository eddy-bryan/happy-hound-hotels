from django.shortcuts import render
from django.views import generic
from .models import Kennel
from .forms import SearchForm

def home(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            num_pets = form.cleaned_data['num_pets']
            # Render the kennel_list.html template only if the form is valid
            return render(request, 'kennel_manager/kennel_list.html', {'form': form})
    else:
        form = SearchForm()
    return render(request, 'kennel_manager/index.html', {'form': form})


class KennelList(generic.ListView):
    queryset = Kennel.objects.all()
    template_name = 'kennel_list.html'


# def kennel_details():