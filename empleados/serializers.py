from rest_framework.serializers import ModelSerializer

from empleados.models import Empleado
from puestos.serializers import PuestoSerializer


class EmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'apellido')


class CreateEmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'


class DetailEmpleadoSerializer(ModelSerializer):
    puesto = PuestoSerializer()

    class Meta:
        model = Empleado
        fields = '__all__'
