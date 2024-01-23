from rest_framework import generics
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaCreateListView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    
class TarefaRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer    