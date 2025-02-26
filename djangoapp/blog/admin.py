from django.contrib import admin

from .models import Postagem, Categoria

class PostagemAdmin(admin.ModelAdmin):
    exclude = ['data']
    prepopulated_fields = {'slug': ('titulo',)}

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Postagem)
admin.site.register(Categoria)