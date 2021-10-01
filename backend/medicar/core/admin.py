from django.contrib import admin


from core.models import EspecialidadeMedica, HorarioAgenda, Medico, AgendaMedica

# Register your models here.
admin.site.register(EspecialidadeMedica)

admin.site.register(Medico)

admin.site.register(AgendaMedica)
admin.site.register(HorarioAgenda)
