from django.contrib import admin
from .models import Produto, Estoque, EstoqueItens

@admin.register(Produto)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'importado',
        'ncm',
        'preco',
        'estoque',
        'estoque_minimo', 
    )
    search_fields=('produto',)
    list_filter= ('importado',)

class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf','funcionario', )
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'

    