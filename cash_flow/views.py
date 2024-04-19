from django.shortcuts import render, redirect
from django.urls import reverse
from .form import RegisterFlows
from django.contrib import messages
from .models import RegisterModel
from utils.getdate import getdatesystem, parse_data
from utils.pagination import make_pagination
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
import csv

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
        'date': actually_data,
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
        'date': search_term
    }

    return render(request, 'cash_flow/pages/flows.html', context)
    
@login_required(login_url='users:login', redirect_field_name='next')
def download_csv(request):
    if not request.POST:
        raise Http404()
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Relatório.csv"'

    writer = csv.writer(response)

    writer.writerow(['Descrição', 'Natureza', 'Tipo', 'Valor'])

    try:
        date = parse_data(request.POST.get('date'))
    except:
        date = request.POST.get('date')

    flows = RegisterModel.objects.filter(created_at__icontains=date).order_by('-created_at')

    nature = ''
    type_cash = ''
    for flow in flows:
        if flow.nature == 'entry':
            nature = 'Entrada'
        elif flow.nature == 'output':
            nature = 'Saida'

        if flow.type_cash == 'din':
            type_cash = 'Dinheiro'
        elif flow.type_cash == 'cc':
            type_cash = 'Cartão de crédito'
        elif flow.type_cash == 'cd':
            type_cash = 'Cartão de débito'
        elif flow.type_cash == 'pix':
            type_cash = 'Pix'
        else:
            type_cash = '-'

        writer.writerow([flow.description, nature, type_cash, flow.value])

    return response  
