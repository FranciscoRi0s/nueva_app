from django.contrib import admin

# Register your models here.
from .models import Informacion
mis_modelos = [Informacion]
for model in mis_modelos:
    admin.site.register(model)