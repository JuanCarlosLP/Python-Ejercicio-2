from rest_framework.viewsets import ModelViewSet

from puestos.models import Puesto
from puestos.serializers import PuestoSerializer, CreatePuestoSerializer


class PuestoViewSet(ModelViewSet):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreatePuestoSerializer
        return PuestoSerializer
