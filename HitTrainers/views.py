from rest_framework import generics, viewsets
from .models import Trainers
from .serializers import TrainersSerializer

class TrainersViewSet(viewsets.ModelViewSet):
    queryset = Trainers.objects.all()
    serializer_class = TrainersSerializer


# примеры без viewset
# class TrainersAPIView(generics.ListCreateAPIView):
#     queryset = Trainers.objects.all()
#     serializer_class = TrainersSerializer
#
# class TrainersAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Trainers.objects.all()
#     serializer_class = TrainersSerializer

