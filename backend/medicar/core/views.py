from django.shortcuts import render
from core.serializers import *
from core.models import *
from django.utils.timezone import now
from core import permissions as core_permissions
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import permissions, viewsets


class EspecialidadeMedicaView(viewsets.ModelViewSet):
    
    queryset = EspecialidadeMedica.objects.all()
    serializer_class = EspecialidadeMedicaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'head']
    def get_queryset(self):
        
        queryset = EspecialidadeMedica.objects.all()
        busca_por_nome = self.request.query_params.get('search', None)
        if busca_por_nome is not None:
            queryset = queryset.filter(nome_especialidade__icontains=busca_por_nome)

        return queryset


class AgendaMedicaListView(viewsets.ModelViewSet):
    
    queryset = AgendaMedica.objects.all()
    serializer_class = AgendaMedicaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = AgendaMedica.objects.filter(dia__gte=now())
        queryset = queryset.filter(horarios__isnull=True)

        data_inicio = self.request.query_params.get('data_inicio', None)
        data_final = self.request.query_params.get('data_final', None)

        if data_inicio:
            data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
            queryset = queryset.filter(dia__gte=data_inicio)

        if data_final:
            data_final = datetime.strptime(data_final, "%Y-%m-%d")
            queryset = queryset.filter(dia__lte=data_final)

        especialidade = self.request.query_params.getlist(
            'especialidade', None)

        medico = self.request.query_params.getlist(
            'medico', None)

        if especialidade:
            queryset = queryset.filter(
                medico__especialidade__id__in=especialidade)

        if medico:
            queryset = queryset.filter(medico__id__in=especialidade)

        return queryset.distinct()


class MedicoView(viewsets.ModelViewSet):

    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = Medico.objects.all()

        busca = self.request.query_params.get('search', None)
        if busca is not None:
            queryset = queryset.filter(nome__icontains=busca)

        especialidade = self.request.query_params.getlist(
            'especialidade', None)

        if especialidade:
            queryset = queryset.filter(especialidade__id__in=especialidade)

        return queryset


class HorarioAgendaView(viewsets.ModelViewSet):

    queryset = HorarioAgenda.objects.all()
    serializer_class = HorarioAgendaSerializer    
    permission_classes = (permissions.IsAuthenticated, core_permissions.IsOnwerOrReadOnly,)
    http_method_names = ['get', 'head']
