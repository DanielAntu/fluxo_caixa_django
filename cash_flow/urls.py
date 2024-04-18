from django.urls import path
from . import views

app_name = 'cash_flow'

urlpatterns = [
    path('', views.home, name='home'),
    path('flows/', views.flows, name='flows'),
    path('flows/search/', views.search_date, name='search_date'),
    path('flows/download_csv/', views.download_csv, name='download_csv'),
]