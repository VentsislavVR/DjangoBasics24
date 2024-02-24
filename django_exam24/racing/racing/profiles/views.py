from django.db.models import Sum

from django.urls import reverse_lazy
from django.views import generic as views

from racing.common.utils import get_profile
from racing.profiles.forms import ProfileCreateForm, ProfileUpdateForm
from racing.profiles.models import Profile

class ProfileCreateView(views.CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/profile-create.html'

    def get_success_url(self):
        return reverse_lazy('catalogue')


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()

        total_price_of_cars = profile.car_set.aggregate(total_price=Sum('price'))['total_price']
        context['total_price_of_cars'] = total_price_of_cars

        return context


class ProfileUpdateView(views.UpdateView):
    model = Profile
    template_name = 'profiles/profile-edit.html'
    form_class = ProfileUpdateForm

    def get_object(self, queryset=None):
        return get_profile()

    def get_success_url(self):
        return reverse_lazy('profile details')


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
