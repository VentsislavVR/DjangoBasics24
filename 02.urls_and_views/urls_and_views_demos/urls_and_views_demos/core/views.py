from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index_no_template(request, *args, **kwargs):
    content = f"<h1>It works</h1> " + \
              f"args={args} <br/>" + \
              f"kwargs={kwargs} <br/>" + \
              f"path = {request.path} <br/>" + \
              f"method = {request.method} <br/>" + \
              f"user = {request.user} <br/>"

    return HttpResponse(
        content,
        # status=201,
        # content_type="application/json"
    )


def index(request, *args, **kwargs):
    #
    context = {
        'title': 'Request data',
        "args": args,
        "kwargs": kwargs,
        "path": request.path,
        "method": request.method,
        "user": request.user
    }
    return render(
        request,
        "core/index.html",
        context,
    )

def redirect_to_soft(request):
    return redirect(
        "https://softuni.bg",
    )

def redirect_to_index(request):
    return redirect(
        'index_no_params'
    )
def redirect_to_index_with_params(request):
    return redirect(
        'index_with_ok_and_slug',
        pk=19,
        slug='some-slug'
    )

# return HttpResponseNotFound()
# def index(request, *args, **kwargs):
#     users_list = get_list_or_404(User) #User.objects.all()
#
#     context = {
#         'args': args,
#         'kwargs': kwargs,
#         'users_list': users_list
#     }
#     return render(
#         request,
#         "core/index.html",
#         context
#     )

def raise_error(request):
    return HttpResponseNotFound()

def raise_exeption(request):
    raise Http404