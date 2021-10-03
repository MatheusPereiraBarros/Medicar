from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime
from core.models import Medico 



class Consulta(models.Model):

    dia = models.DateField(verbose_name="Dia da consulta", auto_now=False, auto_now_add=False, null=True, blank=False)
    horario = models.TimeField(verbose_name="Horário da consulta", auto_now=False, auto_now_add=False, null=True, blank=False)
    data_agendamento = models.DateTimeField(verbose_name="Data do agendamento", auto_now_add=True, null=True, blank=False)
    medico = models.ForeignKey(Medico, verbose_name="Médico da consulta", on_delete=models.CASCADE, null=False, blank=False)


    def clean(self, *args, **kwargs):
        if self.dia < datetime.now().date():
            raise ValidationError("Não é possível marcar consulta para um dia anterior ao atual")
        elif(Consulta.objects.filter(medico=self.medico, dia=self.dia).exists()):
            raise ValidationError("Já existe uma consulta agendada para este médico neste dia")
        else:
            super().save(*args, **kwargs)


    def __str__(self):
        return F"Consulta do {self.medico} em {self.dia}"   
    
    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

