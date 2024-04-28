from rest_framework import serializers
from .models import Informacion

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Informacion
        fields=[
            'id',
            'codigo',
            'nombre',
            'descripcion',
            'estrategia_mitigacion',
        ]