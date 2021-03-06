# Generated by Django 3.2.7 on 2021-10-01 16:10

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EspecialidadeMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_especialidade', models.CharField(max_length=200, verbose_name='Especialidade')),
            ],
        ),
        migrations.CreateModel(
            name='HorarioAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField(verbose_name='Horário')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300, verbose_name='Nome')),
                ('crm', models.BigIntegerField(max_length=50, verbose_name='Número do CRM')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Endereço de e-mail')),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Telefone')),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.especialidademedica', verbose_name='Especialidade de atendimento')),
            ],
        ),
        migrations.CreateModel(
            name='AgendaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(verbose_name='Dia do agendamento')),
                ('data_agendamento', models.DateTimeField(auto_now=True)),
                ('horarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.horarioagenda', verbose_name='Horários')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.medico', verbose_name='Médico')),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
        ),
    ]
