from django.contrib import messages
from django.db.models import Sum, F
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from exam3.profiles.models import Profile
from exam3.web.forms import ReadOnlyExpenseForm
from exam3.web.models import Expense


# Create your views here.
class IndexView(views.CreateView):
    template_name = 'common/home-no-profile.html'
    model = Profile
    fields = ('budget','first_name', 'last_name',)

    def get_template_names(self):
        if Profile.objects.exists():
            return 'common/home-with-profile.html'
        return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        expenses_total = Expense.objects.aggregate(total=Sum('price'))['total'] or 0
        context['expenses'] = Expense.objects.all()

        if profile:
            original_budget = profile.budget + expenses_total
            remaining_budget = profile.budget - expenses_total
            context['original_budget'] = original_budget
            context['remaining_budget'] = remaining_budget

        return context

    def get_success_url(self):
        return reverse_lazy('index')

class CreateExpenseView(views.CreateView):
    model = Expense
    fields = ('title', 'price', 'description', 'image_url')
    template_name = 'expenses/expense-create.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form):
        # Get the profile instance
        profile = Profile.objects.first()

        # Check if there is enough remaining budget
        expense = form.instance
        total_expenses = profile.expense_set.exclude(pk=expense.pk).aggregate(total=Sum('price'))['total'] or 0
        remaining_budget = profile.budget - total_expenses
        if remaining_budget >= expense.price:
            # Deduct the expense amount from the remaining budget
            profile.budget -= expense.price
            profile.save()

            # Set the expense's profile
            expense.profile = profile
            return super().form_valid(form)
        else:
            # If there's not enough budget, display an error message
            messages.error(self.request, "Insufficient remaining budget.")
            return super().form_invalid(form)


class UpdateExpenseView(views.UpdateView):
    model = Expense
    fields = ('title', 'price', 'description', 'image_url')
    template_name = 'expenses/expense-edit.html'

    def get_success_url(self):
        return reverse_lazy('index')


class DeleteExpenseView(views.DeleteView):
    queryset = Expense.objects.all()
    template_name = 'expenses/expense-delete.html'
    fields = ('title', 'price', 'description', 'image_url')

    success_url = reverse_lazy('index')
    form_class = ReadOnlyExpenseForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object

        return kwargs
