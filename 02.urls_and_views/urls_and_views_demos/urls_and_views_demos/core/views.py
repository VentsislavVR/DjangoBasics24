from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404


# Create your views here.
# def index(request, *args, **kwargs):
#     content = f"<h1>It works</h1> " +\
#     f"args={args} <br/>"+\
#     f"kwargs={kwargs} <br/>"+\
#     f"path = {request.path} <br/>"+\
#     f"method = {request.method} <br/>"+\
#     f"user = {request.user} <br/>"
#
#     return HttpResponse(
#         content,
#         status=201,
#         content_type="application/json"
#
#     )
    # return HttpResponseNotFound()
def index(request, *args, **kwargs):
    users_list = get_list_or_404(User) #User.objects.all()

    context = {
        'args': args,
        'kwargs': kwargs,
        'users_list': users_list
    }
    return render(
        request,
        "core/index.html",
        context
    )