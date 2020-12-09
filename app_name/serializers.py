from rest_framework import serializers
from .models import Model1


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model1
        fields = '__all__'
