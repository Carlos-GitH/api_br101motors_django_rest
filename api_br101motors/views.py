from rest_framework import viewsets
from api_br101motors.models import Agendamento, Motos, Proprietario
from api_br101motors.serializer import AgendamentoSerializer, MotosSerializer, ProprietarioSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    
class MotosViewSet(viewsets.ModelViewSet):
    queryset = Motos.objects.all()
    serializer_class = MotosSerializer
    
class ProprietarioViewSet(viewsets.ModelViewSet):
    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer