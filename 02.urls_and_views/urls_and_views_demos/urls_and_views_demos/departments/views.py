import time

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# def index(request):
#     return HttpResponse(f"Hello, world. You're at the departments index.{time.time()}")


# def index2(request, *args, **kwargs):
#     return HttpResponse(f"Response from index2.You're at the departments index2.{time.time()}")
#

def department_details(request,pk):
    return HttpResponse(f"Response from department details with ID {pk}.")
def departments_list(request):
    pass
def department_create(request):
    pass
def department_details_by_name(request,name):
    return HttpResponse(f"Department with name : {name}.")


def index(request, *args, **kwargs):
    return HttpResponse(f"It works args={args} kwargs={kwargs}")
"""
Requests <-> Response:
"""