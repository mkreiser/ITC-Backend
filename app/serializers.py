from rest_framework import serializers
from app.models import Athlete, Event, Meet, Result

class AthleteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Athlete
    fields = ('id', 'gender', 'membership', 'name')

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ('id', 'gender', 'name', 'season', 'relay')

class MeetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meet
    fields = ('id', 'date', 'host', 'location', 'name', 'notes', 'resultURL', 'season', 'splitURL')

class ResultSerializer(serializers.ModelSerializer):
  class Meta:
    model = Result
    fields = ('id', 'athlete', 'distanceResult', 'event', 'meet', 'performance', 'result_membership')
