from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos', views.AlunosViewSet, basename='Alunos')
router.register(r'cursos', views.CursosViewSet, basename='Cursos')

urlpatterns = [
    path('', include(router.urls)),
]
