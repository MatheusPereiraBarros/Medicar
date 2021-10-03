from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from core.models import HorarioAgenda
from core.serializers import HorarioAgendaSerializer
from paciente.serializers import ConsultaSerializer, UserSerializer, GroupSerializer
from paciente.models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConsultaView(viewsets.ModelViewSet):

    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
