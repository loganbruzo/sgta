from django.http import JsonResponse
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()

    data = []
    for u in usuarios:
        data.append({
            'id': u.id,
            'nome': u.nome,
            'email': u.email,
        })

    return JsonResponse(data, safe=False)


def buscar_usuario_por_id(request, id):
    try:
        u = Usuario.objects.get(id=id)

        data = {
            'id': u.id,
            'nome': u.nome,
            'email': u.email,
        }

        return JsonResponse(data)

    except Usuario.DoesNotExist:
        return JsonResponse({'erro': 'Usuário não encontrado'})