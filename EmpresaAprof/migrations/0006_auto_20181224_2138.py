# Generated by Django 2.1.4 on 2018-12-25 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpresaAprof', '0005_auto_20181224_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='nome',
            field=models.CharField(choices=[('166', '166'), ('266', '266'), ('366', '366'), ('466', '466')], max_length=30),
        ),
    ]
