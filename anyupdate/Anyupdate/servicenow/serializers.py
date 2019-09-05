from rest_framework import serializers
from .models import ConfigItem, Incident, Application

from django.contrib.auth.models import User, Group

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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']