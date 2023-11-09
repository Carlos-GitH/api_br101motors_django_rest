# Generated by Django 4.2.7 on 2023-11-09 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_br101motors', '0003_alter_agendamento_id_alter_motos_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='moto',
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='placa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_br101motors.motos'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_br101motors.proprietario'),
        ),
    ]