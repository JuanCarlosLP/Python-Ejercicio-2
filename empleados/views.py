from rest_framework.viewsets import ModelViewSet

from empleados.models import Empleado
from empleados.serializers import EmpleadoSerializer, CreateEmpleadoSerializer


class EmpleadoViewSet(ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateEmpleadoSerializer
        return EmpleadoSerializer
