from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from users.models import User
from users.forms import UserRegisterForm, UserLoginForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('users:login_user'))
    return render(request, 'users/register_user.html', {'form': UserRegisterForm})


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('dogs:index'))
                else:
                    return HttpResponse('Аккаунт неактивен!')
    else:
        form = UserLoginForm()
    return render(request, 'users/login_user.html', {'form': form})


@login_required
def user_profile_view(request):
    user_object = request.user
    context = {
        # 'user_object': user_object,
        'title': f'Ваш профиль, {user_object.first_name}',
        # 'form': UserForm(instance=user_object)
    }
    return render(request, 'users/user_profile_read_only.html', context)
