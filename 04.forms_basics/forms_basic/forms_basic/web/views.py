from django.shortcuts import render, redirect

from forms_basic.web.forms import DemoForm, EmployeeForm
from forms_basic.web.models import Employee


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'GET':
        form = EmployeeForm(
            instance=employee,
        )
    else:
        form = EmployeeForm(
            request.POST,
            instance=employee,
        )
        if form.is_valid():
            form.save()
            return redirect('index_models')

    context = {
        'form': form,
        'employee': employee,
    }
    return render(
        request,
        'web/employee_details.html',
        context
    )


def index_models(request):
    form = EmployeeForm(
        request.POST or None,
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index_models')

    context = {
        'form': form,
        'employees': Employee.objects.all(),
    }
    return render(
        request,
        'web/index_models.html',
        context
    )


def index(request):
    form = DemoForm(
        request.POST or None,
        initial={
            'last_name': 'Rachev',
        }
    )

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data['first_name'])
            return redirect('index')

    context = {
        'employee_form': form,
    }
    return render(
        request,
        'web/index.html',
        context
    )
# Create your views here.
# def index(request):
#     if request.method == 'GET':
#
#         context = {
#             'employee_form': EmployeeForm(),
#         }
#
#         return render(
#             request,
#             'web/index.html',
#             context
#         )
#     else:
#         form = EmployeeForm(request.POST)
#
#         if form.is_valid():
#             # data is valid,populate cleaned_data
#             form.cleaned_data['first_name']
#             # use the data
#             # redirect to some URL
#             return redirect('index')
#         else:
#             context = {
#                 'employee_form': form,
#             }
#             # data is invalid populate errors
#             return render(
#                 request,
#                 'web/index.html',
#                 context
#             )
