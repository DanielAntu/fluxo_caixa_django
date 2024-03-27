from django.shortcuts import render, redirect
from django.urls import reverse
from .form import RegisterFlows
from .models import RegisterModel

def home(request):
    if request.POST:
        form = RegisterFlows(request.POST)
    else:
        form = RegisterFlows()

    if form.is_valid():
        register = form.save(commit=False)
        register.user = request.user
        register.save()
        return redirect(reverse('cash_flow:home'))


    context = {
        'title': 'Home',
        'form': form,
    }

    return render(request, 'cash_flow/pages/home.html', context)

def flows(request):
    context = {
        'title': 'Fluxos'
    }

    return render(request, 'cash_flow/pages/flows.html', context)
