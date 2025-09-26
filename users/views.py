from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid(): # аутентификация пользователя
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active: # авторизация пользователя
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = User(username=cd['username'])
            user.set_password(cd['password'])
            user.save()
            messages.success(request, "Аккаунт создан успешно!")
    else:
      form = RegisterUserForm()

    return render(request, 'register.html', {"form": form})