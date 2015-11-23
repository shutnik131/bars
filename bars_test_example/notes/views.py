from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Tag, Note
from .forms import NoteForm


# Create your views here.


def home_view(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        auth = authenticate(username=username, password=password)
        if auth is not None:
            login(request, auth)
            return HttpResponseRedirect(reverse('notes:index'))
        else:
            messages.add_message(request, messages.INFO, "Авторизация не пройдена!")
            return HttpResponseRedirect(reverse('home'))
    return render_to_response('home.html', RequestContext(request))


def index_view(request):
    notes = Note.objects.all().order_by('-pub_date')
    return render_to_response('index.html', {'notes': notes})


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Note Added!')
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = NoteForm()
    return render_to_response('addnote.html', {'form': form}, RequestContext(request))
