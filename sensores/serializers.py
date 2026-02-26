# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import ReadSensors

class ReadSensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadSensors
        fields = '__all__'