from profile import Profile

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from exam_prep_1.albums.models import Album
from exam_prep_1.profiles.models import Profile
from exam_prep_1.profiles.forms import ProfileCreateForm


class IndexView(views.CreateView):
    template_name = 'common/home-no-profile.html'  # Default template for the index view
    model = Profile
    form_class = ProfileCreateForm


    def get_template_names(self):
        # Check if any profiles exist
        if Profile.objects.exists():
            # If profiles exist, switch to the template with profile
            return ['common/home-with-profile.html']
        else:
            # If no profiles exist, use the default template
            return [self.template_name]
    def get_success_url(self):
        return reverse('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfileCreateForm()
        context['profile'] = Profile.objects.first()
        context['albums'] = Album.objects.all()

        return context

# Create your views here.
class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        # Assuming you want to retrieve the first Profile object
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object

        return context


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = 'profile/profile-delete.html'
    pk_url_kwarg = 'pk'

    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        # Return the profile of the currently logged-in user
        return self.model.objects.first()
