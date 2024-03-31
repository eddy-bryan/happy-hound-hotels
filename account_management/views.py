from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile, PetProfile

def user_profile(request):
    # Retrieve the UserProfile object for the current user
    user_profile = UserProfile.objects.get(username=request.user)
    
    # Filter PetProfile objects based on the current user
    user_pets = PetProfile.objects.filter(owner=request.user)
    
    # Pass the UserProfile and user_pets objects to the template context
    context = {'user_profile': user_profile, 'user_pets': user_pets}
    
    # Render the template with the context
    return render(request, 'account_management/user_profile.html', context)
