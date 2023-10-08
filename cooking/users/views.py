from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .utils import search_profiles, paginator


def users(request):
    profiles, search_query = search_profiles(request)
    custom_range, profiles = paginator(request, profiles, 3)

    context = {
        'profiles': profiles,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'users/profiles.html', context)


def users_details(request, pk):
    prof = Profile.objects.get(id=pk)
    profile_recipe = prof.recipe_set.all()

    context = {
        'profile': prof,
        'profile_recipe': profile_recipe,
    }
    return render(request, 'users/profile.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Имя пользователя не существует')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно зашли в свой аккаунт')
            return redirect('users')
        else:
            messages.error(request, 'Имя пользователя или пароль введены не верно')
    return render(request, 'users/login_user.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'Пользователь вышел из учетной записи')
    return redirect('login_user')


def register_user(request):
    page = 'register'
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Профиль пользователя успешно создан")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Произошла ошибка во время регистрации')

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_user.html', context)


@login_required(login_url='login')
def profile(request):
    account = request.user.profile
    account_recipe = account.recipe_set.all
    context = {
        'account': account,
        'account_recipe': account_recipe,
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_profile(request):
    account = request.user.profile
    form = ProfileForm(instance=account)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно редактировали профиль')
            return redirect('profile')
    context = {
        'form': form,
        'account': account,
    }
    return render(request, 'users/account_form.html', context)
