from django.contrib import admin
from .models import Produto, Categoria, Adicional, Opcoes

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Adicional)
admin.site.register(Opcoes)
