from django.shortcuts import render, redirect
from django.views import generic as views

from exam_doncho.albums.models import Album
from exam_doncho.common.profile_helpers import get_profile

from exam_doncho.web.forms import CreateProfileForm





def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'no_nav': True,
    }

    return render(
        request,
        'web/home-no-profile.html',
        context
    )


# Create your views here.
def index(request):
    profile = get_profile()
    if profile is None:
        return create_profile(request)
    context = {
        'albums':Album.objects.all()
    }

    return render(request, 'web/home-with-profile.html',context)
