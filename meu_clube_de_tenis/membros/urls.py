from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('membros/', views.membros, name='membros'),
    path('membros/detalhes/<int:membro_id>/', views.detalhes, name='detalhes'),
    path('testing/', views.testing, name='testing'),
]
