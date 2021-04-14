from rest_framework.viewsets import ModelViewSet

from permisos.models import Permiso
from permisos.serializers import PermisoSerializer, CreatePermisoSerializer


class PermisoViewSet(ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreatePermisoSerializer
        return PermisoSerializer
