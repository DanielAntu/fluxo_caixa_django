from django.shortcuts import render, redirect
from django.urls import reverse
from .form import RegisterFlows
from django.contrib import messages
from .models import RegisterModel
from utils.getdate import getdatesystem, parse_data
from utils.pagination import make_pagination
from django.http import Http404
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='users:login', redirect_field_name='next')
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
        'button_txt': 'Enviar'
    }

    return render(request, 'cash_flow/pages/home.html', context)

@login_required(login_url='users:login', redirect_field_name='next')
def flows(request):
    actually_data = getdatesystem()

    flows = RegisterModel.objects.filter(created_at__icontains=actually_data).order_by('-created_at')

    page_obj = make_pagination(request, flows)

    context = {
        'flows': page_obj,
        'date_term': getdatesystem(),
        'title': 'Fluxos',
    }

    return render(request, 'cash_flow/pages/flows.html', context)

@login_required(login_url='users:login', redirect_field_name='next')
def search_date(request):
    search_term = request.GET.get('date')

    if not search_term:
        raise Http404()
    
    flows = RegisterModel.objects.filter(created_at__icontains=search_term).order_by('-created_at')

    page_obj = make_pagination(request, flows)

    context = {
        'flows': page_obj,
        'date_term': search_term
    }

    return render(request, 'cash_flow/pages/flows.html', context)
    
@login_required(login_url='users:login', redirect_field_name='next')
def download_csv(request):
    try:
        date = parse_data(request.POST.get('date'))
    except:
        date = request.POST.get('date')

    print(date)


    return redirect(reverse('cash_flow:flows'))    
