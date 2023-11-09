from rest_framework import serializers
from api_br101motors.models import *
from api_br101motors.validators import *

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

        
class ProprietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietario
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError('CPF inválido')
        
        if not validate_nome(data['nome']):
            raise serializers.ValidationError('Nome inválido')
        
        if not validate_telefone(data['telefone']):
            raise serializers.ValidationError({'telefone':'Telefone deve seguir o modelo: XX XXXXX-XXXX'})
        
        return data

class MotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motos
        fields = '__all__'
    def validate_placa(self, placa):
        if len(placa) != 7:
            raise serializers.ValidationError('Placa deve conter 8 digitos')
        return placa
        
class ListaMotosProprietarioSerializer(serializers.ModelSerializer):
    moto = serializers.ReadOnlyField(source='moto.placa')
    class Meta:
        model = Motos
        fields = ['placa', 'modelo', 'cor', 'ano', 'data_cadastro'] 
        
class ListaAgendamentosProprietarioSerializer(serializers.ModelSerializer):
    moto_id = serializers.ReadOnlyField(source='moto.placa')
    proprietario_id = serializers.ReadOnlyField(source='proprietario.nome')
    class Meta:
        model = Agendamento
        fields = '__all__'