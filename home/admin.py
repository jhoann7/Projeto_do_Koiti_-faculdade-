from django.contrib import admin
from .models import Usuario, Produto # Importe o modelo Produto

# Registre o modelo Usuario (se já não estiver registrado)
admin.site.register(Usuario)

# --- Registre o Novo Modelo Produto ---
admin.site.register(Produto)