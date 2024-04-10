from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Kennel, Booking, Review
from .forms import SearchForm, BookingForm, ReviewForm

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


def kennel_detail(request, slug):
    kennel = get_object_or_404(Kennel, slug=slug)
    reviews = kennel.reviews.all().order_by("-created_on")
    review_count = kennel.reviews.all().count()

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.kennel = kennel
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted successfully!'
            )

    review_form = ReviewForm()

    return render(
        request,
        'kennel_manager/kennel_detail.html',
        {
            'kennel': kennel,
            'reviews': reviews,
            'review_count': review_count,
            'review_form': review_form,
        },
    )


def review_edit(request, slug, review_id):
    if request.method == "POST":

        queryset = Kennel.objects.all()
        kennel = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.kennel = kennel
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review updated successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review.')

    return HttpResponseRedirect(reverse('kennel_detail', args=[slug]))


def review_delete(request, slug, review_id):
    queryset = Kennel.objects.all()
    kennel = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted successfully.')
    else:
        messages.add_message(request, messages.ERROR, 'Error deleting review.')

    return HttpResponseRedirect(reverse('kennel_detail', args=[slug]))


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
