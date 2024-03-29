from django.shortcuts import render
from django.views import generic

class UserProfile(generic.TemplateView):
    template_name = 'account_management/user_profile.html'
