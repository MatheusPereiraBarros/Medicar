# Generated by Django 3.2.7 on 2021-10-01 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_agendamedica_horarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamedica',
            name='horarios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.horarioagenda', verbose_name='Horários'),
        ),
    ]
