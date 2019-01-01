from django.db import models



class Curso(models.Model):

     CONTABILIDADE = 'Contabilidade'
     INFORMATICA = 'Informática'
     ADMINISTRACAO = 'Administração'
     ANALISES_CLINICAS = 'Análises Clínicas'
     OUTROS = 'Outros'
    

     cursos_choices = (
     (CONTABILIDADE,'Contabilidade'),
     (INFORMATICA,'Informática'),
     (ADMINISTRACAO, 'Administração'),
     (ANALISES_CLINICAS,'Análises Clínicas'),
     (OUTROS,'Outros'),
     

    )
     nome = models.CharField('nome do curso',max_length=50,choices=cursos_choices)
     carga_horaria = models.IntegerField('carga horária')
     ementa = models.CharField('ementa da disciplina',max_length=50)
     valor = models.FloatField('valor do curso')

     class Meta:
         verbose_name_plural='cursos'
         verbose_name='curso'
         ordering = ('-carga_horaria','valor')

     def __str__(self):
        return '{}'.format(
            self.nome

            )
class Turma(models.Model):

     TURMA1 = '166'
     TURMA2 = '266'
     TURMA3 = '366'
     TURMA4 = '466'  
     turma_choices = (
       (TURMA1, '166'),
       (TURMA2, '266'),
       (TURMA3, '366'),
       (TURMA4, '466'),

        )
     nome = models.CharField(max_length=30,choices=turma_choices)
     data_inicio = models.DateField('data de inicío')
     data_termino = models.DateField('data de término')
     hora_inicio = models.TimeField()
     hora_termino = models.TimeField()

     class Meta:
         verbose_name_plural='turmas'
         verbose_name='turma'
         ordering = ('-data_inicio','data_termino')


     def __str__(self):
        return '{} - {} - {}'.format(
            self.data_inicio.strftime('%d/%m/%Y'),
            self.hora_inicio.strftime('%H:%M'),
            self.nome

            )

class Professor(models.Model):
     RITOMAR = 'RT'
     ROGERIO = 'RG'
     NEY = 'NE'
     VALERIA = 'VL'
     OSIRES = 'OS'

     professores_choices = (
        (RITOMAR,'Ritomar'),
        (ROGERIO,'Rogerio'),
        (NEY,'Ney'),
        (VALERIA,'Valeria'),
        (OSIRES,'Osires'),

     )
     

     nome = models.CharField('nome do professor',max_length=50,choices=professores_choices)
     telefone = models.CharField('telefone do professor',max_length=50)
     valor_hora_aula = models.DecimalField('valor da aula por hora',max_digits=8, decimal_places=2)
     turma = models.ForeignKey(Turma , on_delete = models.CASCADE)

     class Meta:
         verbose_name_plural='professores'
         verbose_name='professor'

         ordering = ('-nome','telefone')


     def __str__(self):
        return '{}'.format(
            self.telefone

            )



