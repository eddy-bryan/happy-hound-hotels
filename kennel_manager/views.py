from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Kennel, Booking, Review
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
                booked_spaces = sum(num_pets for booking in booking_within_dates)
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
    reviews = kennel.reviews.all().order_by("-created_on")
    review_count = kennel.reviews.all().count()

    return render(
        request,
        'kennel_manager/kennel_detail.html',
        {
            'kennel': kennel,
            'reviews': reviews,
            'review_count': review_count,
        },
    )


@login_required
def book_now(request, kennel_id):
    kennel = get_object_or_404(Kennel, pk=kennel_id)
    
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            num_pets = form.cleaned_data['num_pets']

            booking = Booking.objects.create(
                customer=request.user,
                kennel=kennel,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                num_pets=num_pets
            )
                
            # Redirect to booking success page after creating the booking
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(request, 'kennel_manager/booking_form.html', {'form': form, 'kennel': kennel})


def booking_success(request):
    return render(request, 'kennel_manager/booking_success.html')