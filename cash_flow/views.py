from django.shortcuts import render, redirect
from django.urls import reverse
from .form import RegisterFlows
from django.contrib import messages
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
        messages.success(request, 'Registro salvo com sucesso')
        return redirect(reverse('cash_flow:home'))


    context = {
        'title': 'Home',
        'form': form,
    }

    return render(request, 'cash_flow/pages/home.html', context)

def flows(request):
    flows = RegisterModel.objects.all().order_by('-created_at')

    context = {
        'flows': flows,
        'title': 'Fluxos'
    }

    return render(request, 'cash_flow/pages/flows.html', context)
