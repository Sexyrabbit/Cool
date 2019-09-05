from rest_framework.viewsets import ModelViewSet

from .serializers import ConfigItemSerializer, IncidentSerializer, ApplicationSerializer
from .models import ConfigItem, Incident, Application

class ConfigItemViewSet(ModelViewSet):
    queryset = ConfigItem.objects.all()
    serializer_class = ConfigItemSerializer

class IncidentViewSet(ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

