from rest_framework import viewsets
from django.http import JsonResponse
from .serializer import AlunoSerializer, CursoSerializer
from .models import Aluno, Curso

# Create your views here.
class AlunosViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
