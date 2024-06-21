from django.http import JsonResponse

# Create your views here.
def alunos(request):
    try:
        if request.method == 'GET':
            alunos = [
                {
                    'id': 1,
                    'nome': 'João',
                    'idade': 20,
                },
                {
                    'id': 2,
                    'nome': 'Maria',
                    'idade': 22,
                }
            ]
            return JsonResponse({'alunos': alunos})
        else:
            return JsonResponse({'error': 'Método inválido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
