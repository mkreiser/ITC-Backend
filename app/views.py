from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max, Min
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from rest_framework import filters, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Athlete, Event, Meet, Result, News, ModelEnums
from app.serializers import AthleteSerializer, EventSerializer, MeetSerializer, ResultSerializer, ResultSerializerNoDepth, NewsSerializer

import django_filters

# Root page directory
@api_view(('GET',))
@permission_classes((AllowAny,))
def api_root(request, format=None):
    return Response({ "routes": [
      "GET ALL Athletes: https://illinoistrackclub.herokuapp.com/athletes/",
      "GET Athlete: https://illinoistrackclub.herokuapp.com/athletes/getAthlete/[id]/",
      "POST Athlete: https://illinoistrackclub.herokuapp.com/athletes/newAthlete/",
      "PUT Athlete: https://illinoistrackclub.herokuapp.com/athletes/updateAthlete/[id]/",
      "DELETE Athlete: https://illinoistrackclub.herokuapp.com/athletes/deleteAthlete/[id]/",

      "GET Athlete's Results: https://illinoistrackclub.herokuapp.com/athletes/getAthleteResults/[id]/",
      "GET Athlete's PRs: https://illinoistrackclub.herokuapp.com/athletes/getAthleteBests/[id]/",

      "GET ALL Events: https://illinoistrackclub.herokuapp.com/events/",
      "GET Event: https://illinoistrackclub.herokuapp.com/events/getEvent/[id]/",
      "POST Event: https://illinoistrackclub.herokuapp.com/events/newEvent/",
      "PUT Event: https://illinoistrackclub.herokuapp.com/events/updateEvent/[id]/",
      "DELETE Event: https://illinoistrackclub.herokuapp.com/events/deleteEvent/[id]/",

      "GET ALL Top 10 Performances: https://illinoistrackclub.herokuapp.com/events/getTopPerformances/",
      "GET Event Top 10 Performances: https://illinoistrackclub.herokuapp.com/events/getTopPerformances/[event_id]/",

      "GET ALL Records: https://illinoistrackclub.herokuapp.com/events/getRecords/",
      "GET Event Record: https://illinoistrackclub.herokuapp.com/events/getRecords/[event_id]/",

      "GET ALL Meets: https://illinoistrackclub.herokuapp.com/meets/",
      "GET Meet: https://illinoistrackclub.herokuapp.com/meets/getMeet/[id]/",
      "POST Meet: https://illinoistrackclub.herokuapp.com/meets/newMeet/",
      "PUT Meet: https://illinoistrackclub.herokuapp.com/meets/updateMeet/[id]/",
      "DELETE Meet: https://illinoistrackclub.herokuapp.com/meets/deleteMeet/[id]/",

      "GET ALL Results: https://illinoistrackclub.herokuapp.com/results/",
      "GET Result: https://illinoistrackclub.herokuapp.com/results/getResult/[id]/",
      "POST Result: https://illinoistrackclub.herokuapp.com/results/newResult/",
      "PUT Result: https://illinoistrackclub.herokuapp.com/results/updateResult/[id]/",
      "DELETE Result: https://illinoistrackclub.herokuapp.com/results/deleteResult/[id]/",

      "GET ALL News: https://illinoistrackclub.herokuapp.com/news/",
      "GET News: https://illinoistrackclub.herokuapp.com/news/getNews/[id]/",
      "POST News: https://illinoistrackclub.herokuapp.com/news/newNews/",
      "PUT News: https://illinoistrackclub.herokuapp.com/news/updateNews/[id]/",
      "DELETE News: https://illinoistrackclub.herokuapp.com/news/deleteNews/[id]/",

      "Logout: https://illinoistrackclub.herokuapp.com/logout"
    ]})

# ATHLETE FILTERS
class AthleteFilter(django_filters.FilterSet):
  class Meta:
    model = Athlete
    fields = ['gender', 'membership', 'name']

# ATHLETE SERIALIZERS
class AthleteGETAll(generics.ListAPIView):
  permission_classes = (AllowAny, )
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer
  filter_backends = (filters.SearchFilter,)
  search_fields = ['name']

class AthleteGET(generics.RetrieveAPIView):
  permission_classes = (AllowAny, )
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer

class AthletePOST(generics.CreateAPIView):
  permission_classes = (IsAdminUser, )
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer

class AthletePUT(generics.RetrieveUpdateAPIView):
  permission_classes = (IsAdminUser, )
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer

class AthleteDELETE(generics.DestroyAPIView):
  permission_classes = (IsAdminUser, )
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer

# EVENT FILTERS
class EventFilter(django_filters.FilterSet):
  class Meta:
    model = Event
    fields = ['gender', 'distanceEvent', 'name', 'season', 'relay']

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
  permission_classes = (IsAdminUser, )
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class EventPUT(generics.RetrieveUpdateAPIView):
  permission_classes = (IsAdminUser, )
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class EventDELETE(generics.DestroyAPIView):
  permission_classes = (IsAdminUser, )
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
  permission_classes = (IsAdminUser, )
  queryset = Meet.objects.all()
  serializer_class = MeetSerializer

class MeetPUT(generics.RetrieveUpdateAPIView):
  permission_classes = (IsAdminUser, )
  queryset = Meet.objects.all()
  serializer_class = MeetSerializer

class MeetDELETE(generics.DestroyAPIView):
  permission_classes = (IsAdminUser, )
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
  permission_classes = (IsAdminUser, )
  queryset = Result.objects.all()
  serializer_class = ResultSerializerNoDepth

class ResultPUT(generics.RetrieveUpdateAPIView):
  permission_classes = (IsAdminUser, )
  queryset = Result.objects.all()
  serializer_class = ResultSerializerNoDepth

class ResultDELETE(generics.DestroyAPIView):
  permission_classes = (IsAdminUser, )
  queryset = Result.objects.all()
  serializer_class = ResultSerializer

# NEWS FITLER
class NewsFilter(django_filters.FilterSet):
  class Meta:
    model = News
    fields = {
            'author': ['contains'],
            'post_datetime': ['year'],
            'post_subject': ['contains'],
            'post_season': ['contains'],
            'post_text': ['contains']
        }

# NEWS SERIALIZERS
class NewsGETAll(generics.ListAPIView):
  queryset = News.objects.all()
  serializer_class = NewsSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = NewsFilter

class NewsGET(generics.RetrieveAPIView):
  queryset = News.objects.all()
  serializer_class = NewsSerializer

class NewsPOST(generics.CreateAPIView):
  permission_classes = (IsAdminUser, )
  queryset = News.objects.all()
  serializer_class = NewsSerializer

class NewsPUT(generics.RetrieveUpdateAPIView):
  permission_classes = (IsAdminUser, )
  queryset = News.objects.all()
  serializer_class = NewsSerializer

class NewsDELETE(generics.DestroyAPIView):
  permission_classes = (IsAdminUser, )
  queryset = News.objects.all()
  serializer_class = NewsSerializer


# RECORD PERFORMANCE
@api_view(['GET'])
def GETRecords(request):
  data = {
    "Indoor": [],
    "Outdoor": [],
    "XC": []
  }

  for event in Event.objects.all().order_by('season'):
    data[event.season].append({
      "name": event.name,
      "record": getRecord(event.pk)
    })

  return Response(data)

@api_view(['GET'])
def GETRecord(request, pk):
  return Response(getRecord(pk))

# RECORD PERFORMANCE HELPER
def getRecord(pk):
  event = Event.objects.get(pk=pk)

  if (event.gender == ModelEnums.BOTH):
    maleRecord = getRecordByGender(event.result_set.all(), ModelEnums.MALE, event.distanceEvent)
    femaleRecord = getRecordByGender(event.result_set.all(), ModelEnums.FEMALE, event.distanceEvent)

    maleRecordSerialized = ResultSerializer(maleRecord, many=True)
    femaleRecordSerialized = ResultSerializer(femaleRecord, many=True)

    return { "maleRecord": maleRecordSerialized.data, "femaleRecord": femaleRecordSerialized.data }
  elif (event.gender == ModelEnums.MALE):
    maleRecord = getRecordByGender(event.result_set.all(), ModelEnums.MALE, event.distanceEvent)

    maleRecordSerialized = ResultSerializer(maleRecord, many=True)
    return { "maleRecord": maleRecordSerialized.data }
  else:
    femaleRecord = getRecordByGender(event.result_set.all(), ModelEnums.FEMALE, event.distanceEvent)

    femaleRecordSerialized = ResultSerializer(femaleRecord, many=True)
    return { "femaleRecord": femaleRecordSerialized.data }


def getRecordByGender(events, gender, isDistance):
  performance = '-performance' if isDistance else 'performance'
  return Result.objects.filter(id__in=events, athlete__gender=gender).order_by(performance)[:1]

# TOP PERFORMANCES
@api_view(['GET'])
@cache_page(60 * 20)
def GETEventTopPerformances(request):
  data = {
    "Indoor": [],
    "Outdoor": [],
    "XC": []
  }

  for event in Event.objects.all().order_by('season'):
    data[event.season].append({
      "name": event.name,
      "performances": getTopPerformances(event.pk)
    })

  return Response(data)

@api_view(['GET'])
def GETEventTopPerformance(request, pk):
  return Response(getTopPerformances(pk))

# TOP PERFORMANCE HELPERS
def getTopPerformanceByGender(events, gender, isDistance):
  performance = '-performance' if isDistance else 'performance'
  return Result.objects.filter(id__in=events, athlete__gender=gender).order_by(performance).distinct(athlete)[:10]


def getTopPerformances(pk):
  event = Event.objects.get(pk=pk)

  if (event.gender == ModelEnums.BOTH):
    maleRecords = getTopPerformanceByGender(event.result_set.all(), ModelEnums.MALE, event.distanceEvent)
    femaleRecords = getTopPerformanceByGender(event.result_set.all(), ModelEnums.FEMALE, event.distanceEvent)

    maleRecords = ResultSerializer(maleRecords, many=True)
    femaleRecords = ResultSerializer(femaleRecords, many=True)

    return { "maleRecords": maleRecords.data, "femaleRecords": femaleRecords.data }
  elif (event.gender == ModelEnums.MALE):
    maleRecords = getTopPerformanceByGender(event.result_set.all(), ModelEnums.MALE, event.distanceEvent)
    maleRecords = ResultSerializer(maleRecords, many=True)

    return { "maleRecords": maleRecords.data }
  else:
    femaleRecords = getTopPerformanceByGender(event.result_set.all(), ModelEnums.FEMALE, event.distanceEvent)
    femaleRecords = ResultSerializer(femaleRecords, many=True)

    return { "femaleRecords": femaleRecords.data }

@api_view(['GET'])
@cache_page(60 * 20)
def GETAthletePerformances(request, pk):
  athlete = Athlete.objects.filter(pk=pk)

  data = {
    "Indoor": [],
    "Outdoor": [],
    "XC": []
  }

  for event in Event.objects.all().order_by('season'):
    performance = '-performance' if event.distanceEvent else 'performance'
    results = ResultSerializer(Result.objects.filter(athlete=athlete, event=event).order_by(performance), many=True)

    if (results.data != []):
      data[event.season].append({
        "name": event.name,
        "performances": results.data
      })

  return Response(data)

@api_view(['GET'])
@cache_page(60 * 20)
def GETAthleteBestPerformances(request, pk):
  athlete = Athlete.objects.filter(pk=pk)

  data = {
    "Indoor": [],
    "Outdoor": [],
    "XC": []
  }

  for event in Event.objects.all().order_by('season'):
    performance = '-performance' if event.distanceEvent else 'performance'
    results = ResultSerializer(Result.objects.filter(athlete=athlete, event=event).order_by(performance)[:1], many=True)

    if (results.data != []):
      data[event.season].append({
        "name": event.name,
        "performances": results.data
      })

  return Response(data)
