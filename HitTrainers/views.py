from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Trainers
from .pagination import TrainersAPIViewPagination
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import TrainersSerializer


class TrainersAPIView(generics.ListCreateAPIView):
     queryset = Trainers.objects.all()
     serializer_class = TrainersSerializer
     permission_classes = (IsAuthenticatedOrReadOnly,)
     pagination_class = TrainersAPIViewPagination

class TrainersAPIDestroy(generics.RetrieveDestroyAPIView):
     queryset = Trainers.objects.all()
     serializer_class = TrainersSerializer
     # просматривать могут все, а удалять только админ
     permission_classes = (IsAdminOrReadOnly,)

class TrainersAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Trainers.objects.all()
    serializer_class = TrainersSerializer
    # изменять только свою запись пользователю, а читать всем
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

