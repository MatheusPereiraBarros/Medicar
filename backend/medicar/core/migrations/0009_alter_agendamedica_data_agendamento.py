# Generated by Django 3.2.7 on 2021-10-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211001_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamedica',
            name='data_agendamento',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
