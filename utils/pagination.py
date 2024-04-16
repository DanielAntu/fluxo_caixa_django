from django.core.paginator import Paginator

def make_pagination(request, flows, per_page=12):
    paginator = Paginator(flows, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj