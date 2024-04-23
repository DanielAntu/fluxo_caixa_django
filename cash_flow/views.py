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
def relatorio(request, date):
    flows = RegisterModel.objects.filter(created_at__icontains=date)

    soma_entry = 0.0
    soma_output = 0.0
    soma_cc = 0.0
    soma_cd = 0.0
    soma_din = 0.0
    soma_pix = 0.0
    for flow in flows:
        flow.value = float(flow.value.replace(',', '.'))
        if flow.nature == 'entry':
            soma_entry += flow.value
        elif flow.nature == 'output':
            soma_output += flow.value

        if flow.type_cash == 'cc':
            soma_cc += flow.value
        elif flow.type_cash == 'cd':
            soma_cd += flow.value
        elif flow.type_cash == 'din':
            soma_din += flow.value
        elif flow.type_cash == 'pix':
            soma_pix += flow.value


    dif_total = soma_entry - soma_output

    context = {
        'soma_entry': f'{soma_entry:.2f}',
        'soma_output': f'{soma_output:.2f}',
        'dif_total': f'{dif_total:.2f}',
        'soma_cc': f'{soma_cc:.2f}',
        'soma_cd': f'{soma_cd:.2f}',
        'soma_din': f'{soma_din:.2f}',
        'soma_pix': f'{soma_pix:.2f}'
    }

    return render(request, 'cash_flow/pages/relatorio.html', context)
    
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
