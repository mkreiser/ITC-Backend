from django.db import models

# Create your models here.

class ModelEnums (models.Model):
  BOTH = 'Both'
  MALE = 'Male'
  FEMALE =  'Female'
  GENDER_OPTIONS = (
    (MALE, MALE),
    (FEMALE, FEMALE)
  )

  EVENT_GENDER_OPTIONS = (
    (BOTH, BOTH),
    (MALE, MALE),
    (FEMALE, FEMALE)
  )

  CLUB = 'Club'
  ALUM = 'Alum'
  ELITE = 'Elite'
  MEMBERSHIP_OPTIONS = (
    (CLUB, CLUB),
    (ALUM, ALUM),
    (ELITE, ELITE)
  )

  XC = 'XC'
  INDOOR = 'Indoor'
  OUTDOOR = 'Outdoor'
  SEASON_OPTIONS = (
    (XC, XC),
    (INDOOR, INDOOR),
    (OUTDOOR, OUTDOOR)
  )

# Create your models here.
class Athlete (models.Model):
  gender = models.CharField(max_length = 10, choices = ModelEnums.GENDER_OPTIONS)
  membership = models.CharField(max_length = 10, choices = ModelEnums.MEMBERSHIP_OPTIONS, default = ModelEnums.CLUB)
  name = models.CharField(max_length = 50)

  def __str__(self):
    return self.name

class Event (models.Model):
  distanceEvent = models.BooleanField(default = False)
  gender = models.CharField(max_length = 10, choices = ModelEnums.EVENT_GENDER_OPTIONS, default = ModelEnums.BOTH)
  name = models.CharField(max_length = 50)
  relay = models.BooleanField(default = False)
  season = models.CharField(max_length = 10, choices = ModelEnums.SEASON_OPTIONS)

  def __str__(self):
    return self.name + '(' + self.season + ', ' + self.gender + ')'

class Meet (models.Model):
  date = models.DateField()
  host = models.CharField(max_length = 50)
  location = models.CharField(max_length = 50)
  name = models.CharField(max_length = 100)
  notes = models.TextField(blank=True)
  resultURL = models.TextField(blank=True)
  season = models.CharField(max_length = 10, choices = ModelEnums.SEASON_OPTIONS)
  splitURL = models.TextField(blank=True)

  def __str__(self):
    return self.name + ', ' + self.location + ', ' + self.date

class Result (models.Model):
  athlete = models.ManyToManyField(Athlete)
  distanceResult = models.BooleanField(default = False)
  event = models.ForeignKey(Event, on_delete = models.DO_NOTHING)
  meet = models.ForeignKey(Meet, on_delete = models.DO_NOTHING)
  performance = models.FloatField(null = False)
  result_membership = models.CharField(max_length = 6, choices = ModelEnums.MEMBERSHIP_OPTIONS, default = ModelEnums.CLUB)

  def __str__(self):
    return str(self.athlete + ', ' + self.performance)

