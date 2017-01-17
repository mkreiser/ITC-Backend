from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max, Min

from rest_framework import filters, status, generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Athlete, Event, Meet, Result, News, ModelEnums
from app.serializers import AthleteSerializer, EventSerializer, MeetSerializer, ResultSerializer, ResultSerializerNoDepth, NewsSerializer

import django_filters

# Root page directory
@api_view(('GET',))
def api_root(request, format=None):
    return Response({ "routes": [
      "GET ALL Athletes: http://localhost:8000/athletes/",
      "GET Athlete: http://localhost:8000/athletes/getAthlete/[id]/",
      "POST Athlete: http://localhost:8000/athletes/newAthlete/",
      "PUT Athlete: http://localhost:8000/athletes/updateAthlete/[id]/",
      "DELETE Athlete: http://localhost:8000/athletes/deleteAthlete/[id]/",

      "GET ALL Events: http://localhost:8000/events/",
      "GET Event: http://localhost:8000/events/getEvent/[id]/",
      "POST Event: http://localhost:8000/events/newEvent/",
      "PUT Event: http://localhost:8000/events/updateEvent/[id]/",
      "DELETE Event: http://localhost:8000/events/deleteEvent/[id]/",

      "GET ALL Top 10 Performances: http://localhost:8000/events/getTopPerformances/",
      "GET Event Top 10 Performances: http://localhost:8000/events/getTopPerformances/[event_id]/",

      "GET ALL Records: http://localhost:8000/events/getRecords/",
      "GET Event Record: http://localhost:8000/events/getRecords/[event_id]/",

      "GET ALL Meets: http://localhost:8000/meets/",
      "GET Meet: http://localhost:8000/meets/getMeet/[id]/",
      "POST Meet: http://localhost:8000/meets/newMeet/",
      "PUT Meet: http://localhost:8000/meets/updateMeet/[id]/",
      "DELETE Meet: http://localhost:8000/meets/deleteMeet/[id]/",

      "GET ALL Results: http://localhost:8000/results/",
      "GET Result: http://localhost:8000/results/getResult/[id]/",
      "POST Result: http://localhost:8000/results/newResult/",
      "PUT Result: http://localhost:8000/results/updateResult/[id]/",
      "DELETE Result: http://localhost:8000/results/deleteResult/[id]/",

      "GET ALL News: http://localhost:8000/news/",
      "GET News: http://localhost:8000/news/getNews/[id]/",
      "POST News: http://localhost:8000/news/newNews/",
      "PUT News: http://localhost:8000/news/updateNews/[id]/",
      "DELETE News: http://localhost:8000/news/deleteNews/[id]/",
    ]})

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
  serializer_class = ResultSerializerNoDepth

class ResultPUT(generics.RetrieveUpdateAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializerNoDepth

class ResultDELETE(generics.DestroyAPIView):
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
  queryset = News.objects.all()
  serializer_class = NewsSerializer

class NewsPUT(generics.RetrieveUpdateAPIView):
  queryset = News.objects.all()
  serializer_class = NewsSerializer

class NewsDELETE(generics.DestroyAPIView):
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
  return Result.objects.filter(id__in=events, athlete__gender=gender).order_by(performance).distinct()[:10]


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
