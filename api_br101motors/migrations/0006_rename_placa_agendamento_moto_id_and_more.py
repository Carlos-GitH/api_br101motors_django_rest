# Generated by Django 4.2.7 on 2023-11-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_br101motors', '0005_alter_proprietario_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='placa',
            new_name='moto_id',
        ),
        migrations.RenameField(
            model_name='agendamento',
            old_name='proprietario',
            new_name='proprietario_id',
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
