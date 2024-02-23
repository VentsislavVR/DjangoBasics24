from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from exam3.profiles.models import Profile
from exam3.web.models import Expense


# Create your views here.
class DetailsProfileView(views.ListView):
    queryset = Profile.objects.first()
    template_name = 'profile/profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['expenses'] = Expense.objects.all()
        context['og_budget'] = Expense.objects.all().aggregate(total=Sum('price'))['total'] or 0
        # total_expenses = Expense.objects.aggregate(total=Sum('price'))['total'] or 0
        #
        # budget = context['profile'].budget if context['profile'] else 0
        #
        # remaining_budget = budget - total_expenses
        # context['remaining_budget'] = remaining_budget

        return context


class EditProfileView(views.UpdateView):
    model = Profile
    fields = ('budget','first_name', 'last_name',)

    template_name = 'profile/profile-edit.html'
    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_success_url(self):
        return redirect('index')


class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = 'profile/profile-delete.html'
    success_url = 'index'
    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_success_url(self):
        return reverse_lazy('index')