from rest_framework import viewsets, generics
from api_br101motors.models import Agendamento, Motos, Proprietario
from api_br101motors.serializer import AgendamentoSerializer, MotosSerializer, ProprietarioSerializer, ListaMotosProprietarioSerializer, ListaAgendamentosProprietarioSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class MotosViewSet(viewsets.ModelViewSet):
    queryset = Motos.objects.all()
    serializer_class = MotosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ProprietarioViewSet(viewsets.ModelViewSet):
    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListaMotosProprietario(generics.ListAPIView):
    def get_queryset(self):
        queryset = Motos.objects.filter(proprietario_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMotosProprietarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListaAgendamentosProprietario(generics.ListAPIView):
    def get_queryset(self):
        queryset = Agendamento.objects.filter(proprietario_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAgendamentosProprietarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]