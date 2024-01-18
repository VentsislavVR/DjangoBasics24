import datetime
import random

from django.shortcuts import render

class Person:
    def __init__(self, first_name, last_name,age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
# Create your views here.
def index(request):
    context = {
        "title": 'Employees list',  # valid
        "new.employee": 'John Doe',  # invalid
        "new employee": 'John Doe',  # invalid
        "names": ["Gosho", "Ivan", "Pesho"],  # valid
        'ages': [random.randrange(1, 100) for _ in range(10)],

        "person": {
            "first_name": "John",
            "last_name": "Doe",
            'age':None
        },
        'person_obj': Person('John', 'Doe'),
        'date': datetime.date.today(),
        'get_params': request.GET,

    }
    return render(
        request,
        'employees/index.html',
        context)
def employee_details(request, pk):
    context={
        'pk':pk,
    }
    return render(
        request,
        "employees/employee_details.html",
        context
    )