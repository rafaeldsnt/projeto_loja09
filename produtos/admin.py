from django.contrib import admin

# Register your models here.
from .models import Produto

#user admin senha: 123456

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'data_criacao')
    search_fields = ('nome',)
    list_filter = ('data_criacao',)
