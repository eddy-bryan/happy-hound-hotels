from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile, PetProfile

def user_profile(request):
    user_profile = UserProfile.objects.get(username=request.user)
    user_pets = PetProfile.objects.filter(owner=request.user)
    context = {'user_profile': user_profile, 'user_pets': user_pets}
    return render(request, 'account_management/user_profile.html', context)


# def pet_profile(request, owner, pet_name):
#     pet_name = PetProfile.objects.get(pet_name=pet_name)
#     owner = UserProfile.objects.get(username=request.user)
#     context = {'pet_name': pet_name, 'owner': owner}
#     return render(request, 'account_management/pet_profile.html', context)


def pet_profile(request, owner, pet_name):
    pet_profile = PetProfile.objects.get(owner__username=owner, pet_name=pet_name)
    owner_profile = UserProfile.objects.get(username__username=owner)
    context = {'pet_profile': pet_profile, 'owner_profile': owner_profile}
    return render(request, 'account_management/pet_profile.html', context)

