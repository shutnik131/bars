from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import RegisterForm
from .models import Author

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            if user['password'] == user['password1']:
                new_author = Author.objects.create(username=user['username'], password=user['password'])
                new_author.save()
                return HttpResponseRedirect('/notes/')
            else:
                pass
    else:
        form = RegisterForm()
    return render_to_response('home.html', {'form': form}, RequestContext(request))

def notes(request):
    return render_to_response('notes.html')