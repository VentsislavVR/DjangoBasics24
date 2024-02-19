from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from exam_doncho.common.profile_helpers import get_profile
from exam_doncho.profiles.models import Profile



# Create your views here.
class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
