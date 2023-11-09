from rest_framework import serializers
from api_br101motors.models import *

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'
        
class ProprietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietario
        fields = '__all__'

class MotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motos
        fields = '__all__'