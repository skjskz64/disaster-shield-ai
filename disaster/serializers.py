from rest_framework import serializers
from .models import *

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '_all_'


class DisasterPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterPrediction
        fields = '_all_'