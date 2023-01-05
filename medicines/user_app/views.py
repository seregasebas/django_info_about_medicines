from django.http import JsonResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, HttpResponseRedirect

from .forms import RegistrationForm
from django.views.generic import CreateView, DetailView
from .models import MedUser
from rest_framework.authtoken.models import Token

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'user_app/login.html'

class UserCreateView(CreateView):
    model = MedUser
    template_name = 'user_app/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user:login')

class UserDetailView(DetailView):
    model = MedUser
    template_name = 'user_app/profile.html'


def update_token(request):
    user = request.user
    # сделал через try/except, т.к. через if выдает ошибку, 
    # когда у юзера еще нет токена в базе и он создается впервые
    try:
        # если уже есть
        if user.auth_token:
            # обновить
            user.auth_token.delete()
            Token.objects.create(user=user)
    except:
        # создать
        Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('user:profile', kwargs={'pk': user.pk}))


def update_token_ajax(request):
    user = request.user
    try:
        # если уже есть
        if user.auth_token:
            # обновить
            user.auth_token.delete()
            token = Token.objects.create(user=user)
    except:
        # создать
        token = Token.objects.create(user=user)
    return JsonResponse({'key': token.key})
