from django.shortcuts import render, redirect
from django.urls import reverse
from .form import RegisterFlows
from django.contrib import messages
from .models import RegisterModel
from utils.getdate import getdatesystem
from django.http import Http404

def home(request):
    if request.POST:
        form = RegisterFlows(request.POST)
    else:
        form = RegisterFlows()

    if form.is_valid():
        register = form.save(commit=False)
        register.user = request.user
        register.save()
        messages.success(request, 'Registro salvo com sucesso')
        return redirect(reverse('cash_flow:home'))


    context = {
        'title': 'Home',
        'form': form,
    }

    return render(request, 'cash_flow/pages/home.html', context)

def flows(request):
    actually_data = getdatesystem()

    flows = RegisterModel.objects.filter(created_at__icontains=actually_data).order_by('-created_at')

    context = {
        'flows': flows,
        'date': actually_data,
        'title': 'Fluxos',
    }

    return render(request, 'cash_flow/pages/flows.html', context)

def search_date(request):
    search_term = request.GET.get('date')

    if not search_term:
        raise Http404()
    
    flows = RegisterModel.objects.filter(created_at__icontains=search_term).order_by('-created_at')

    context = {
        'flows': flows,
        'date': search_term
    }

    return render(request, 'cash_flow/pages/flows.html', context)
    
    
