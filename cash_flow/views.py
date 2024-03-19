from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home'
    }

    return render(request, 'cash_flow/pages/home.html', context)

def flows(request):
    context = {
        'title': 'Fluxos'
    }

    return render(request, 'cash_flow/pages/flows.html', context)
