from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import filters, status, generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Athlete, Event, Meet, Result, News, ModelEnums
from app.serializers import AthleteSerializer, EventSerializer, MeetSerializer, ResultSerializer, NewsSerializer

import django_filters

# Root page directory
@api_view(('GET',))
def api_root(request, format=None):
    return Response({ "routes": [
      "GET ALL Athletes: http://illinoistrackclub.herokuapp.com/athletes/",
      "GET Athlete: http://illinoistrackclub.herokuapp.com/athletes/getAthlete/[id]/",
      "POST Athlete: http://illinoistrackclub.herokuapp.com/athletes/newAthlete/",
      "PUT Athlete: http://illinoistrackclub.herokuapp.com/athletes/updateAthlete/[id]/",
      "DELETE Athlete: http://illinoistrackclub.herokuapp.com/athletes/deleteAthlete/[id]/",

      "GET ALL Events: http://illinoistrackclub.herokuapp.com/events/",
      "GET Event: http://illinoistrackclub.herokuapp.com/events/getEvent/[id]/",
      "POST Event: http://illinoistrackclub.herokuapp.com/events/newEvent/",
      "PUT Event: http://illinoistrackclub.herokuapp.com/events/updateEvent/[id]/",
      "DELETE Event: http://illinoistrackclub.herokuapp.com/events/deleteEvent/[id]/",

      "GET ALL Top 10 Performances: http://illinoistrackclub.herokuapp.com/events/getTopPerformances",
      "GET Event Top 10 Performances: http://illinoistrackclub.herokuapp.com/events/getTopPerformances/[event_id]/",

      "GET ALL Meets: http://illinoistrackclub.herokuapp.com/meets/",
      "GET Meet: http://illinoistrackclub.herokuapp.com/meets/getMeet/[id]/",
      "POST Meet: http://illinoistrackclub.herokuapp.com/meets/newMeet/",
      "PUT Meet: http://illinoistrackclub.herokuapp.com/meets/updateMeet/[id]/",
      "DELETE Meet: http://illinoistrackclub.herokuapp.com/meets/deleteMeet/[id]/",

      "GET ALL Results: http://illinoistrackclub.herokuapp.com/results/",
      "GET Result: http://illinoistrackclub.herokuapp.com/results/getResult/[id]/",
      "POST Result: http://illinoistrackclub.herokuapp.com/results/newResult/",
      "PUT Result: http://illinoistrackclub.herokuapp.com/results/updateResult/[id]/",
      "DELETE Result: http://illinoistrackclub.herokuapp.com/results/deleteResult/[id]/",

      "GET ALL News: http://illinoistrackclub.herokuapp.com/news/",
      "GET News: http://illinoistrackclub.herokuapp.com/news/getNews/[id]/",
      "POST News: http://illinoistrackclub.herokuapp.com/news/newNews/",
      "PUT News: http://illinoistrackclub.herokuapp.com/news/updateNews/[id]/",
      "DELETE News: http://illinoistrackclub.herokuapp.com/news/deleteNews/[id]/",
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
  serializer_class = ResultSerializer

class ResultPUT(generics.RetrieveUpdateAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializer

class ResultDELETE(generics.DestroyAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializer

# NEWS FITLER
class NewsFilter(django_filters.FilterSet):
  class Meta:
    model = News
    fields = ['author', 'post_subject', 'post_datetime', 'post_season']

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


# HELPER FUNCTIONS

# TOP PERFORMANCE HELPERS
def getTopPerformanceByGender(events, gender, isDistance):
  performance = '-performance' if isDistance else 'performance'
  return Result.objects.filter(id__in=events, athlete__gender=gender).order_by(performance)[:10]


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
