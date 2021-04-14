from rest_framework.viewsets import ModelViewSet

from empleados.models import Empleado
from empleados.serializers import EmpleadoSerializer, CreateEmpleadoSerializer, DetailEmpleadoSerializer


class EmpleadoViewSet(ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return CreateEmpleadoSerializer
        if self.action == 'retrieve':
            return DetailEmpleadoSerializer
        return EmpleadoSerializer
