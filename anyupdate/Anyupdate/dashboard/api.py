from rest_framework.viewsets import ModelViewSet

from .serializers import STSerializer, CISerializer, APPSerializer
from .models import support_team, configure_item, application

class STViewSet(ModelViewSet):
    queryset = support_team.objects.all()
    serializer_class = STSerializer

class CIViewSet(ModelViewSet):
    queryset = configure_item.objects.all()
    serializer_class = CISerializer

class APPViewSet(ModelViewSet):
    queryset = application.objects.all()
    serializer_class = APPSerializer