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

# Root page directory
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
      "GET ALL Athletes": "http://mighty-lowlands-90976.herokuapp.com/athletes/",
      "GET Athlete": "http://mighty-lowlands-90976.herokuapp.com/athletes/getAthlete/[id]/",
      "POST Athlete": "http://mighty-lowlands-90976.herokuapp.com/athletes/newAthlete/",
      "PUT Athlete": "http://mighty-lowlands-90976.herokuapp.com/athletes/updateAthlete/[id]/",
      "DELETE Athlete": "http://mighty-lowlands-90976.herokuapp.com/athletes/deleteAthlete/[id]/",

      "GET ALL Events": "http://mighty-lowlands-90976.herokuapp.com/events/",
      "GET Event": "http://mighty-lowlands-90976.herokuapp.com/events/getEvent/[id]/",
      "POST Event": "http://mighty-lowlands-90976.herokuapp.com/events/newEvent/",
      "PUT Event": "http://mighty-lowlands-90976.herokuapp.com/events/updateEvent/[id]/",
      "DELETE Event": "http://mighty-lowlands-90976.herokuapp.com/events/deleteEvent/[id]/",

      "GET ALL Meets": "http://mighty-lowlands-90976.herokuapp.com/meets/",
      "GET Meet": "http://mighty-lowlands-90976.herokuapp.com/meets/getMeet/[id]/",
      "POST Meet": "http://mighty-lowlands-90976.herokuapp.com/meets/newMeet/",
      "PUT Meet": "http://mighty-lowlands-90976.herokuapp.com/meets/updateMeet/[id]/",
      "DELETE Meet": "http://mighty-lowlands-90976.herokuapp.com/meets/deleteMeet/[id]/",

      "GET ALL Results": "http://mighty-lowlands-90976.herokuapp.com/results/",
      "GET Result": "http://mighty-lowlands-90976.herokuapp.com/results/getResult/[id]/",
      "POST Result": "http://mighty-lowlands-90976.herokuapp.com/results/newResult/",
      "PUT Result": "http://mighty-lowlands-90976.herokuapp.com/results/updateResult/[id]/",
      "DELETE Result": "http://mighty-lowlands-90976.herokuapp.com/results/deleteResult/[id]/",
    })

# ATHLETE FILTERS
class AthleteFilter(django_filters.FilterSet):
  class Meta:
    model = Athlete
    fields = ['gender', 'membership', 'name']

# ATHLETE SERIALIZERS
class AthleteGETAll(generics.ListAPIView):
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer
  filter_backends = (filters.SearchFilter,)
  search_fields = ['name']

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

# EVENT FILTERS
class EventFilter(django_filters.FilterSet):
  class Meta:
    model = Event
    fields = ['gender', 'name', 'season', 'relay']

# EVENT SERIALIZERS
class EventGETAll(generics.ListAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = EventFilter

class EventGET(generics.RetrieveAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class EventPOST(generics.CreateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class EventPUT(generics.RetrieveUpdateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class EventDELETE(generics.DestroyAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

# MEET FILTER
class MeetFilter(django_filters.FilterSet):
  class Meta:
    model = Meet
    fields = ['date', 'host', 'location', 'name', 'season']

# MEET SERIALIZERS
class MeetGETAll(generics.ListAPIView):
  queryset = Meet.objects.all()
  serializer_class = MeetSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = MeetFilter

class MeetGET(generics.RetrieveAPIView):
  queryset = Meet.objects.all()
  serializer_class = MeetSerializer

class MeetPOST(generics.CreateAPIView):
  queryset = Meet.objects.all()
  serializer_class = MeetSerializer

class MeetPUT(generics.RetrieveUpdateAPIView):
  queryset = Meet.objects.all()
  serializer_class = MeetSerializer

class MeetDELETE(generics.DestroyAPIView):
  queryset = Meet.objects.all()
  serializer_class = MeetSerializer

# RESULT FITLER
class ResultFilter(django_filters.FilterSet):
  class Meta:
    model = Result
    fields = ['athlete', 'distanceResult', 'event', 'meet', 'result_membership']

# RESULT SERIALIZERS
class ResultGETAll(generics.ListAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = ResultFilter

class ResultGET(generics.RetrieveAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializer

class ResultPOST(generics.CreateAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializer

class ResultPUT(generics.RetrieveUpdateAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializer

class ResultDELETE(generics.DestroyAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializer
