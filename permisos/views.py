from rest_framework.viewsets import ModelViewSet

from permisos.models import Permiso
from permisos.serializers import PermisoSerializer, CreatePermisoSerializer, DetailPermisoSerializer


class PermisoViewSet(ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return CreatePermisoSerializer
        if self.action == 'retrieve':
            return DetailPermisoSerializer
        return PermisoSerializer
