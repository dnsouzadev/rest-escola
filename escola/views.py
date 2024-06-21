from rest_framework import viewsets, generics
from django.http import JsonResponse
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer
from .models import Aluno, Curso, Matricula

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


class MatriculasViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing.
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAno(generics.ListAPIView):
    """
    Listing all enrollments
    """

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer
