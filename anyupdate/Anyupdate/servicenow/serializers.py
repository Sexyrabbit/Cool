from rest_framework import serializers
from .models import ConfigItem, Incident, Application


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'


class ConfigItemSerializer(serializers.ModelSerializer):
    incs = IncidentSerializer(read_only=True, many=True)

    class Meta:
        model = ConfigItem
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    configitem = ConfigItemSerializer(read_only=True, many=True)

    class Meta:
        model = Application
        fields = '__all__'