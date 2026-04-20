<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.http import JsonResponse
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()

    data = []
    for t in tarefas:
        data.append({
            'id': t.id,
            'titulo': t.titulo,
            'status': t.status,
            'usuario': t.usuario_responsavel.nome if t.usuario_responsavel else None
        })

    return JsonResponse(data, safe=False)
>>>>>>> 65029bc0 (primeiro commit)
