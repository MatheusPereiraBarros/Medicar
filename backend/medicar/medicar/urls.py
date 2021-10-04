from collections import namedtuple
from django import urls
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
import paciente
import paciente.views as paciente_views
import core.views as core_views
from rest_framework.authtoken import views as atviews
from django.contrib import admin

from core.serializers import AgendaMedicaSerializer, EspecialidadeMedicaSerializer, MedicoSerializer
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', paciente_views.UserViewSet)
router.register(r'consultas', paciente_views.ConsultaView)
router.register(r'especialidades', core_views.EspecialidadeMedicaView)
router.register(r'agendas', core_views.AgendaMedicaListView)
router.register(r'lista-medicos', core_views.MedicoView)
router.register(r'horarios', core_views.HorarioAgendaView)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'obter-token/', atviews.obtain_auth_token, name='token'),
]