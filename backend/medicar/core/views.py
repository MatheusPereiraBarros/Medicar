from django.shortcuts import render
from core.serializers import *
from core.models import *

from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets


class EspecialidadeMedicaView(viewsets.ModelViewSet):
    queryset = EspecialidadeMedica.objects.all()
    serializer_class = EspecialidadeMedicaSerializer


class AgendaMedicaView(viewsets.ModelViewSet):
    queryset = AgendaMedica.objects.all()
    serializer_class = AgendaMedicaSerializer


class MedicoView(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class HorarioAgendaView(viewsets.ModelViewSet):

    queryset = HorarioAgenda.objects.all()
    serializer_class = HorarioAgendaSerializer