from rest_framework import viewsets
from .models import *
from .serializers import *

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer


class DisasterPredictionViewSet(viewsets.ModelViewSet):
    queryset = DisasterPrediction.objects.all()
    serializer_class = DisasterPredictionSerializer