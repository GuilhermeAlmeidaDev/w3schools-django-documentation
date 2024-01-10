from django.contrib import admin
from .models import Membro

class MembroAdmin(admin.ModelAdmin):
    list_display = ('primeiro_nome', 'ultimo_nome', 'telefone', 'entrou_em')

# Register your models here.
admin.site.register(Membro, MembroAdmin)
