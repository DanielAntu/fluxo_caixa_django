from django.shortcuts import render
from .form import RegisterFlows

def home(request):
    form = RegisterFlows()

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
