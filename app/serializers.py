from rest_framework import serializers
from app.models import Athlete, Event, Meet, Result, News

class AthleteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Athlete
    fields = ('id', 'gender', 'membership', 'name')

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ('id', 'distanceEvent', 'gender', 'name', 'season', 'relay')

class MeetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meet
    fields = ('id', 'date', 'host', 'location', 'name', 'notes', 'resultURL', 'season', 'splitURL')

class ResultSerializer(serializers.ModelSerializer):
  class Meta:
    model = Result
    fields = ('id', 'athlete', 'distanceResult', 'event', 'meet', 'performance', 'result_membership')
    depth = 1

class NewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = News
    fields = ('id', 'author', 'post_subject', 'post_text', 'post_datetime', 'post_season')