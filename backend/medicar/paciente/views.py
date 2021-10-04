from django.contrib.auth.models import User, Group
from django.http import response
from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework.response import Response
from core.models import HorarioAgenda
from core.serializers import HorarioAgendaSerializer
from paciente.serializers import ConsultaSerializer, UserSerializer, GroupSerializer
from paciente.models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.utils.timezone import now
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })




class ConsultaView(viewsets.ModelViewSet):

    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    http_method_names = ['get', 'head', 'post', 'delete']
