from django.shortcuts import render, redirect
from django.urls import reverse
from .form import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    
    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )

        if authenticated_user is not None:
            messages.success(request, 'Logado com sucesso')
            login(request, authenticated_user)
            return redirect(reverse('cash_flow:home'))
        else:
            messages.error(request, 'Seu usuário ou senha estão incorretas')
            
    context = {
        'form': form
    }

    return render(request, 'users/login.html', context)

@login_required(login_url='users:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('users:login'))
    
    if request.POST.get('username') != request.user.username:
        return redirect(reverse('users:login'))
    
    logout(request)
    return redirect(reverse('users:login'))