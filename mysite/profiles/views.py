from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def home(request):
    context = locals()
    template = 'profiles/home.html'
    return render(request, template, context)

from django.views.generic.base import TemplateView
#--- TemplateView
class HomeTV(TemplateView):
    template_name = 'profiles/home.html'

class AboutTV(TemplateView):
    template_name = 'profiles/about.html'

@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'profiles/profile.html'
    return render(request, template, context)