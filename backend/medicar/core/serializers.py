from django.db.models import fields
from rest_framework import serializers
from core.models import *



class EspecialidadeMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspecialidadeMedica
        fields = ('nome_especialidade',)


class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeMedicaSerializer(read_only=False) 
    class Meta:
        model = Medico
        fields = ('id', 'nome', 'crm', 'email', 'telefone', 'especialidade')


class HorarioAgendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HorarioAgenda
        fields = ('horario',)

class AgendaMedicaSerializer(serializers.ModelSerializer):

    horarios = HorarioAgendaSerializer(many=True, read_only=True)
    medico = MedicoSerializer(read_only=True)

    class Meta:
        model = AgendaMedica
        fields = ('id', 'dia', 'horarios', 'data_agendamento', 'medico',)