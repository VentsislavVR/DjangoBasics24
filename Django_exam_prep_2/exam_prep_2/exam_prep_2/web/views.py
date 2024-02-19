from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from exam_prep_2.web import forms
from exam_prep_2.web.forms import ReadOnlyPlantForm
from exam_prep_2.web.models import Profile, Plant


# Create your views here.
class IndexView(views.ListView):
    model = Profile
    template_name = "common/home-page.html"  # Default template name is set to home-page.html

    def dispatch(self, request, *args, **kwargs):
        if self.model.objects.exists():  # Check if there's at least one profile object
            return redirect('catalogue')  # Redirect to the catalogue URL
        else:
            return super().dispatch(request, *args, **kwargs)  # Render the default template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.model.objects.first()
        context["plants"] = Plant.objects.all()
        return context


class ProfileCreateView(views.CreateView):
    template_name = "profile/create-profile.html"
    model = Profile
    form_class = forms.ProfileCreateForm

    def get_success_url(self):
        return reverse('index')



class ProfileDetailsView(views.DetailView):
    model = Profile

    template_name = "profile/profile-details.html"
    def get_object(self, queryset=None):

        return Profile.objects.first()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["plants"] = Plant.objects.all()
        return context


class ProfileEditView(views.UpdateView):
    model = Profile
    template_name = "profile/edit-profile.html"
    fields = '__all__'
    def get_object(self, queryset=None):

        return Profile.objects.first()
    def get_success_url(self):
        return reverse('index')


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = "profile/delete-profile.html"
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):

        return Profile.objects.first()


class CatalogueView(views.ListView):
    queryset = Plant.objects.all()
    template_name = "common/catalogue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["plants"] = Plant.objects.all()
        context["profile"] = Profile.objects.first()
        return context



class PlantCreateView(views.CreateView):
    model = Plant
    template_name = "plant/create-plant.html"
    fields = ['plant_type', 'name', 'image_url', 'description', 'price']

    def form_valid(self, form):
        # Get the only Profile object available in the database
        profile = Profile.objects.first()
        # Set the profile field of the Plant object
        form.instance.profile = profile
        # Save the form and return the result
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('catalogue')


class PlantDetailsView(views.DetailView):
    queryset = Plant.objects.all()
    template_name = "plant/plant-details.html"
    pk_url_kwarg = 'pk'


class PlantEditView(views.UpdateView):
    model = Plant
    template_name = "plant/edit-plant.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse('catalogue')


class PlantDeleteView(views.DeleteView):
    model = Plant
    template_name = "plant/delete-plant.html"
    success_url = reverse_lazy('catalogue')
    form_class = ReadOnlyPlantForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.get_object())
        return context


