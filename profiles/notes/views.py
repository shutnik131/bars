from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect("/notes/")
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
                return HttpResponseRedirect('/notes/')
            else:
                return HttpResponse("Ваш аккаунт неактивен")
        else:
            return HttpResponse("Неправильная пара логин/пароль.")
    else:
        form = AuthenticationForm()
    return render_to_response('login.html', {'form': form}, RequestContext(request))



def notes(request):
    return render_to_response('notes.html')
