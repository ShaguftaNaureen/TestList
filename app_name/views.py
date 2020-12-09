from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Model1
from .serializers import ModelSerializer


# Create your views here.
class modelList(APIView):

    def get(self, request):
        model1 = Model1.objects.all()
        serializers = ModelSerializer(model1, many=True)
        return Response(serializers.data)

    def post(self):
        pass