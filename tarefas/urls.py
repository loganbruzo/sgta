from django.urls import path
from .views import listar_tarefas

urlpatterns = [
    path('', listar_tarefas),
]