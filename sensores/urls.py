# -*- coding: utf-8 -*-

from django.urls import path
from .views import receber_leitura,dashboard, grafico_sensores
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard),
    path('api/leituras/', receber_leitura),
    #path('dashboard/', dashboard),
    path('logout/', auth_views.LogoutView.as_view(next_page='/admin/login/'), name='logout'),
    path('graficos/', grafico_sensores,name='grafico_sensores'),
]