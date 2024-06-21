from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos', views.AlunosViewSet, basename='Alunos')
router.register(r'cursos', views.CursosViewSet, basename='Cursos')
router.register(r'matriculas', views.MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', views.ListaMatriculasAno.as_view()),
    path('curso/<int:pk>/matriculas/', views.ListaAlunosMatriculados.as_view())
]
