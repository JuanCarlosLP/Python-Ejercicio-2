from rest_framework.serializers import ModelSerializer

from puestos.models import Puesto


class PuestoSerializer(ModelSerializer):
    class Meta:
        model = Puesto
        fields = ('id', 'nombre', 'descripcion')

class CreatePuestoSerializer(ModelSerializer):
    class Meta:
        model = Puesto
        fields = '__all__'
