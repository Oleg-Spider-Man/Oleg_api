from rest_framework import serializers
from .models import Trainers


class TrainersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Trainers
        fields = ('__all__')
