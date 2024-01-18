import datetime

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

        "person": {
            "first_name": "John",
            "last_name": "Doe",
            'age':None
        },
        'person_obj': Person('John', 'Doe'),
        'date': datetime.date.today(),

    }
    return render(
        request,
        'employees/index.html',
        context)
