from rest_framework import viewsets
from todos_app.models import Task
from todos_app.serializer import PublicTaskSerializer


# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
    """Exibe todas as tasks criadas. 
    Um viewset fornece e lida automaticamente com os métodos padrões: GET, POST, etc...
    Essa é a grande mágica do DRF"""

    queryset = Task.objects.all()
    serializer_class = PublicTaskSerializer