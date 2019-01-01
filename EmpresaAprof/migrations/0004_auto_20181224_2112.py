# Generated by Django 2.1.4 on 2018-12-25 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpresaAprof', '0003_auto_20181224_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='nome',
            field=models.CharField(choices=[('T1', '166'), ('T2', '266'), ('T3', '366'), ('T4', '466')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='professor',
            name='nome',
            field=models.CharField(choices=[('RT', 'Ritomar'), ('RG', 'Rogerio'), ('NE', 'Ney'), ('VL', 'Valeria'), ('OS', 'Osires')], max_length=50, verbose_name='nome do professor'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='valor_hora_aula',
            field=models.DecimalField(choices=[('V1', 'R$100,00'), ('V2', 'R$200,00'), ('V3', 'R$300,00')], decimal_places=2, max_digits=8, verbose_name='valor da aula por hora'),
        ),
    ]