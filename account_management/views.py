from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile

def user_profile(request):
    user_profile = UserProfile.objects.get(username=request.user)
    context = {'user_profile': user_profile}
    return render(request, 'account_management/user_profile.html', context)
