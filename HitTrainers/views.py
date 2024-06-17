from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import  generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Trainers
from .serializers import TrainersSerializer


# Create your views here.
class TrainersAPIView(generics.ListCreateAPIView):
    queryset = Trainers.objects.all()
    serializer_class = TrainersSerializer

class TrainersAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainers.objects.all()
    serializer_class = TrainersSerializer

#class TrainersAPIView(APIView):
#    def get(self, request):
#        lst = Trainers.objects.all().values()
#        return Response({'get': list(lst)})
#    def post(self, request):
#        new_tr = Trainers.objects.create(
#            name=request.data['name'],
#            second_name=request.data['second_name'],
#            salary=request.data['salary'],
#            experience=request.data['experience'],
#            gender_tr_id=request.data['gender_tr_id']
#        )
#        return Response({'post': model_to_dict(new_tr)})