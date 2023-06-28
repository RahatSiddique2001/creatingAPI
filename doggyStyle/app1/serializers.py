from rest_framework import serializers
from .models import Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name', 'color', 'size', 'friendliness')

