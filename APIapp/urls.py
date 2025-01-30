from django.urls import path
from .views import visualizarTodos, visualizarUm, criar, editar, apagar

urlpatterns = [
    path('artigos/criar/', criar, name="Criar"),
    path('artigos/', visualizarTodos, name="visualizarTodos"),
    path('artigos/editar/<int:artigo_id>/', editar, name='editar'),
    path('artigos/apagar/<int:artigo_id>/', apagar, name='apagar'),
    path('artigos/<int:artigo_id>/', visualizarUm, name='visualizarUm'),
]