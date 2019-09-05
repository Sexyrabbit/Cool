from rest_framework import serializers
from .models import support_team, configure_item, application


class STSerializer(serializers.ModelSerializer):

    class Meta:
        model = support_team
        fields = '__all__'


class CISerializer(serializers.ModelSerializer):

    class Meta:
        model = configure_item
        fields = '__all__'


class APPSerializer(serializers.ModelSerializer):
    class Meta:
        model = application
        fields = '__all__'