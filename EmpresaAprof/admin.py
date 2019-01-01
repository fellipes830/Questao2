from django.contrib import admin
from EmpresaAprof.models import Curso,Turma,Professor



admin.site.site_header = 'Administração de Cursos'
admin.site.site_title = 'Cursos profissionais'
admin.site.index_title = 'Courses'

class ProfessorInline(admin.TabularInline):
    model = Professor


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('data','data_inicio','data_termino','hora_inicio','hora_termino')
    inlines = [ProfessorInline,]
    date_hierarchy = 'data_inicio'
    list_filter = ('data_inicio','data_termino',)
    def data(self,obj):
        return obj.data_inicio.strftime('%d/%m/%Y')
        data.short_description = 'data_inicio'


class CursoAdmin(admin.ModelAdmin):
	list_display = ('nome','carga_horaria','ementa','valor')


admin.site.register(Curso,CursoAdmin)
admin.site.register(Turma,TurmaAdmin)

