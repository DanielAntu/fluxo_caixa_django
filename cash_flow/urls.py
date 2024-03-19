from django.urls import path
from . import views

app_name = 'cash_flow'

urlpatterns = [
    path('', views.home, name='home'),
    path('flows/', views.flows, name='flows'),
]