# Generated by Django 2.1.4 on 2018-12-24 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmpresaAprof', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ('-carga_horaria', 'valor'), 'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'ordering': ('-nome', 'telefone'), 'verbose_name': 'professor', 'verbose_name_plural': 'professores'},
        ),
        migrations.AlterModelOptions(
            name='turma',
            options={'ordering': ('-data_inicio', 'data_termino'), 'verbose_name': 'turma', 'verbose_name_plural': 'turmas'},
        ),
        migrations.AddField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EmpresaAprof.Professor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='carga_horaria',
            field=models.IntegerField(verbose_name='carga horária'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='ementa',
            field=models.CharField(max_length=50, verbose_name='ementa da disciplina'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(choices=[('CT', 'Contabilidade'), ('IN', 'Informática'), ('AD', 'Administração'), ('AN', 'Análises Clínicas'), ('OU', 'Outros')], max_length=50, verbose_name='nome do curso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='valor',
            field=models.FloatField(verbose_name='valor do curso'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='nome do professor'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='telefone',
            field=models.CharField(max_length=50, verbose_name='telefone do professor'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='valor_hora_aula',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='valor da aula por hora'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='data_inicio',
            field=models.DateField(verbose_name='data de inicío'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='data_termino',
            field=models.DateField(verbose_name='data de término'),
        ),
    ]