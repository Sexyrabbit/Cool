from rest_framework.viewsets import ModelViewSet

from .serializers import ConfigItemSerializer, IncidentSerializer, ApplicationSerializer, UserSerializer, GroupSerializer
from .models import ConfigItem, Incident, Application

from django.contrib.auth.models import User, Group


class ConfigItemViewSet(ModelViewSet):
    queryset = ConfigItem.objects.all()
    serializer_class = ConfigItemSerializer


class IncidentViewSet(ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer