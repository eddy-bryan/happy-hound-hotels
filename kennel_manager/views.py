from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Kennel, Booking
from .forms import SearchForm, BookingForm

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


def kennel_detail(request, slug):
    kennel = get_object_or_404(Kennel, slug=slug)
    return render(request, 'kennel_manager/kennel_detail.html', {'kennel': kennel})


def book_now(request, kennel_id):
    kennel = get_object_or_404(Kennel, pk=kennel_id)
    if request.method == 'POST':
        print(request.POST)
        form = BookingForm(user=request.user, data=request.POST)
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            selected_pets = form.cleaned_data.get('pet_name')

            # Initialise a list to store booking data
            bookings_data = []

            # Create booking data for each selected pet
            for pet in selected_pets:
                booking_data = {
                    'customer': request.user,
                    'kennel': kennel,
                    'check_in_date': check_in_date,
                    'check_out_date': check_out_date,
                    'pet_name': pet
                }
                bookings_data.append(booking_data)

            # Create Booking instances from the collected data
            for booking_data in bookings_data:
                Booking.objects.create(**booking_data)

            Booking.objects.save()

            # Redirect to booking success page after creating all bookings
            return redirect('booking_success')
    else:
        form = BookingForm(user=request.user)
    return render(request, 'kennel_manager/booking_form.html', {'form': form, 'kennel': kennel})
