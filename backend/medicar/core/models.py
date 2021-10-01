from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F
from phonenumber_field.modelfields import PhoneNumberField


class EspecialidadeMedica(models.Model):

    nome_especialidade = models.CharField(verbose_name="Especialidade", max_length=200, blank=False, null=False)

    def __str__(self):
        return f'{self.nome_especialidade}'

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = "Especialidades médicas"


class Medico(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=300, blank=False, null=False)
    crm = models.BigIntegerField(verbose_name="Número do CRM", blank=False, null=False)
    email = models.EmailField(verbose_name="Endereço de e-mail", null=True, blank=True)
    telefone = PhoneNumberField(verbose_name="Telefone", null=True, blank=True)
    especialidade = models.ForeignKey(EspecialidadeMedica, verbose_name="Especialidade de atendimento", null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'


class HorarioAgenda(models.Model):
    horario = models.TimeField(verbose_name="Horário")
    
    def __str__(self):
        return F"Horário: {self.horario}"

    class Meta:
        verbose_name = "Horário"
        verbose_name_plural = "Horários"

class AgendaMedica(models.Model):

    medico = models.ForeignKey(Medico, verbose_name="Médico", null=False, blank=False, on_delete=models.CASCADE)
    dia = models.DateField(verbose_name="Dia do agendamento", null=False, blank=False)
    data_agendamento = models.DateTimeField(auto_now=True, null=False, blank=False)
    horarios = models.ManyToManyField(HorarioAgenda, verbose_name="Horários")



    
    def clean(self, *args, **kwargs):
        if self.dia < datetime.now().date():
            raise ValidationError("Não é possível criar agenda para um dia anterior ao atual")
        elif(AgendaMedica.objects.filter(medico=self.medico, dia=self.dia).exists()):
            raise ValidationError("Já existe uma agenda para este médico neste dia")
        else:
            super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
        
    def __str__(self):
        return F"Agenda do {self.medico} em {self.dia}"

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"


