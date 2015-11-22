from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Author
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = Author(form.save())
            return HttpResponseRedirect("/notes/")
    else:
        form = UserCreationForm()
    return render_to_response('register.html', {'form': form}, RequestContext(request))


def notes(request):
    return render_to_response('notes.html')
