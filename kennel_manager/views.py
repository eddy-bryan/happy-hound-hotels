from django.shortcuts import render
from django.views import generic
from .models import Kennel, Booking
from .forms import SearchForm

def home(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            num_pets = int(form.cleaned_data['num_pets'])
            # Filter the queryset based on search criteria
            available_kennels = []
            for kennel in Kennel.objects.all():
                booking_within_dates = Booking.objects.filter(
                    kennel=kennel,
                    check_in_date__lte=check_out_date,
                    check_out_date__gte=check_in_date
                )
                booked_spaces = sum(booking.pet_name.count() for booking in booking_within_dates)
                if kennel.spaces - booked_spaces >= num_pets:
                    available_kennels.append(kennel)
            # Render the kennel_list.html template with filtered queryset
            return render(request, 'kennel_manager/kennel_list.html', {'kennels': available_kennels, 'form': form})
    else:
        form = SearchForm()
    return render(request, 'kennel_manager/index.html', {'form': form})

class KennelList(generic.ListView):
    template_name = 'kennel_list.html'



# class KennelDetail():