from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import filters, status, generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Athlete, Event, Meet, Result
from app.serializers import AthleteSerializer, EventSerializer, MeetSerializer, ResultSerializer

import django_filters

class AthleteGETAll(generics.ListAPIView):
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer

class AthleteGET(generics.RetrieveAPIView):
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer

class AthletePOST(generics.CreateAPIView):
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer

class AthletePUT(generics.RetrieveUpdateAPIView):
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer

class AthleteDELETE(generics.DestroyAPIView):
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer

