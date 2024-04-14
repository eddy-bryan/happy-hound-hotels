from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Kennel, Booking, Review
from .forms import SearchForm, BookingForm, ReviewForm


def home(request):
    """
    View function for the home page.

    Renders the home page with search form and available kennels based on
    search criteria.
    """
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            # Process the search form data
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            num_pets = int(form.cleaned_data['num_pets'])

            # Filter available kennels based on search criteria
            available_kennels = []
            for kennel in Kennel.objects.all():
                booking_within_dates = Booking.objects.filter(
                    kennel=kennel,
                    check_in_date__lte=check_out_date,
                    check_out_date__gte=check_in_date
                )
                booked_spaces = sum(
                    num_pets
                    for booking in booking_within_dates
                )
                if kennel.spaces - booked_spaces >= num_pets:
                    available_kennels.append(kennel)

            # Render the kennel_list.html template with filtered queryset
            return render(
                request,
                'kennel_manager/kennel_list.html',
                {'kennels': available_kennels, 'form': form}
            )
    else:
        form = SearchForm()
    return render(request, 'kennel_manager/index.html', {'form': form})


def kennel_detail(request, slug):
    """
    View function for the kennel detail page.

    Renders the kennel detail page with kennel information, reviews, and a form
    to submit a review.
    """
    kennel = get_object_or_404(Kennel, slug=slug)
    reviews = kennel.reviews.all().order_by("-created_on")
    review_count = kennel.reviews.all().count()

    if request.method == 'POST':
        # Process the review submission form
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
    """
    View function for editing a review.

    Allows authenticated users to edit their reviews.
    """
    if request.method == "POST":
        # Process the review edit form submission
        queryset = Kennel.objects.all()
        kennel = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.kennel = kennel
            review.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Review updated successfully.'
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating review.'
            )

    return HttpResponseRedirect(reverse('kennel_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    View function for deleting a review.

    Allows authenticated users to delete their reviews.
    """
    queryset = Kennel.objects.all()
    kennel = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        # Delete the review if the authenticated user is the author
        review.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Review deleted successfully.'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Error deleting review.'
        )

    return HttpResponseRedirect(reverse('kennel_detail', args=[slug]))


@login_required
def book_now(request, kennel_id):
    """
    View function for booking a kennel.

    Allows authenticated users to book a kennel.
    """
    kennel = get_object_or_404(Kennel, pk=kennel_id)

    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            num_pets = form.cleaned_data['num_pets']

            # Create a new booking
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

    return render(
        request,
        'kennel_manager/booking_form.html',
        {'form': form, 'kennel': kennel}
    )


def booking_success(request):
    """
    View function for booking success page.

    Renders the booking success page after a successful booking.
    """
    return render(request, 'kennel_manager/booking_success.html')
