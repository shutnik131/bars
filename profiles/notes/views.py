from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NoteForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render_to_response('register.html', {'form': form}, RequestContext(request))


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                request.session['user_id'] = user.id
                return HttpResponseRedirect('/add_note/')
            else:
                return HttpResponse("Ваш аккаунт неактивен")
        else:
            messages.add_message(request, messages.INFO, "Неправильный логин или пароль!")
            return HttpResponseRedirect(reverse('login'))
    else:
        form = AuthenticationForm()
    return render_to_response('login.html', {'form': form}, RequestContext(request))


@login_required
def add_notes(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/notes/")
    else:
        form = NoteForm()
    return render_to_response('add_note.html', {'form': form}, RequestContext(request))


def notes(request):
    return render_to_response('notes')
