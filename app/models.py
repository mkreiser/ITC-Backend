from django.db import models


MALE = 'Male'
FEMALE =  'Female'
GENDER_OPTIONS = (
  (MALE, 'Male'),
  (FEMALE, 'Female')
)

CLUB = 'Club'
ALUM = 'Alum'
ELITE = 'Elite'
MEMBERSHIP_OPTIONS = (
  (CLUB, 'Club'),
  (ALUM, 'Alum'),
  (ELITE, 'Elite')
)

XC = 'XC'
INDOOR = 'Indoor'
OUTDOOR = 'Outdoor'
SEASON_OPTIONS = (
  (XC, 'XC'),
  (INDOOR, 'Indoor'),
  (OUTDOOR, 'Outdoor')
)

# Create your models here.
class Athlete (models.Model):
  name = models.CharField(max_length = 50)
  gender = models.CharField(max_length = 10, choices = GENDER_OPTIONS)
  membership = models.CharField(max_length = 10, choices = MEMBERSHIP_OPTIONS, default = CLUB)

  def __str__(self):
    return self.name

class Event (models.Model):
  name = models.CharField(max_length = 50)
  season = models.CharField(max_length = 10, choices = SEASON_OPTIONS)
  relay = models.BooleanField(default = False)

  def __str__(self):
    return self.name

class Meet (models.Model):
  date = models.DateField()
  host = models.CharField(max_length = 50)
  location = models.CharField(max_length = 50)
  name = models.CharField(max_length = 100)
  notes = models.TextField()
  resultURL = models.TextField()
  season = models.CharField(max_length = 10, choices = SEASON_OPTIONS)
  splitURL = models.TextField()

  def __str__(self):
    return self.name

class Result (models.Model):
  athlete = models.ForeignKey(Athlete, on_delete = models.DO_NOTHING)
  distanceResult = models.BooleanField(default = False)
  event = models.ForeignKey(Event, on_delete = models.DO_NOTHING)
  meet = models.ForeignKey(Meet, on_delete = models.DO_NOTHING)
  result = models.FloatField(null = False)
  result_membership = models.CharField(max_length = 6, choices = MEMBERSHIP_OPTIONS, default = CLUB)

  def __str__(self):
    return self.result
