from django.urls import include, path
from rest_framework import routers
import paciente
import paciente.views as paciente_views
import core.views as core_views

from core.serializers import AgendaMedicaSerializer, EspecialidadeMedicaSerializer, MedicoSerializer
from paciente.serializers import ConsultaSerializer
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


router = routers.DefaultRouter()
router.register(r'users', paciente_views.UserViewSet)
router.register(r'groups', paciente_views.GroupViewSet)
router.register(r'especialidades', core_views.EspecialidadeMedicaView)
router.register(r'agenda-medica', core_views.AgendaMedicaView)
router.register(r'medicos', core_views.MedicoView)
router.register(r'horarios', core_views.HorarioAgendaView)




urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]