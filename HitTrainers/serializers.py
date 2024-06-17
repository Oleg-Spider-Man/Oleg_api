from rest_framework import serializers
from .models import Trainers


class TrainersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainers
        fields = ('__all__')
