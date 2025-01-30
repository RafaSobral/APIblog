import json 
from .models import Artigo
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse


# Create your views here.


def visualizarTodos(request):
    artigos = list(Artigo.objects.values())
    return JsonResponse(artigos, safe=False)


def visualizarUm(request, artigo_id):
    try:
        artigo = Artigo.objects.values().get(id=artigo_id)
        return JsonResponse(artigo)
    except Artigo.DoesNotExist:
        return JsonResponse({'error': 'Artigo nao encontrado'}, status=404)

@csrf_exempt
def criar(request):
    if request.method == "POST":
        try: 
            data = json.loads(request.body)
            artigo = Artigo.objects.create(**data)
            return JsonResponse({'id': artigo.id, 'message': 'Post created'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def editar(request, artigo_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            artigo = Artigo.objects.get(id=artigo_id)
            for key, value in data.items():
                setattr(artigo, key, value)
            artigo.save()
            return JsonResponse({'message': 'Artigo Editado'})
        except Artigo.DoesNotExist:
            return JsonResponse({'error': 'Artigo nao encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def apagar(request, artigo_id):
    if request.method == "DELETE":
        try:
            artigo = Artigo.objects.get(id=artigo_id)
            artigo.delete()
            return HttpResponse(status=204)
        except Artigo.DoesNotExist:
            return JsonResponse({'error': 'Artigo nao encontrado'}, status=404)
