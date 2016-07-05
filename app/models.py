from django.db import models

# Create your models here.
class Athlete (models.Model):
  gender_options = (
    ('Male', 'Male'),
    ('Female', 'Female')
  )

  membership_options = (
    ('Club', 'Club'),
    ('Alum', 'Alum'),
    ('Elite', 'Elite')
  )

  name = models.CharField(max_length = 50)
  gender = models.CharField(max_length = 10, choices = gender_options)
  membership = models.CharField(max_length = 10, choices = membership_options)

  def __str__(self):
    return self.name

class Event (models.Model):
  season_options = (
    ('XC', 'XC'),
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor')
  )

  name = models.CharField(max_length = 50)
  season = models.CharField(max_length = 10, choices = season_options)
  relay = models.BooleanField(default = False)

  def __str__(self):
    return self.name

class Meet (models.Model):
  season_options = (
    ('XC', 'XC'),
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor')
  )

  date = models.DateField()
  host = models.CharField(max_length = 50)
  location = models.CharField(max_length = 50)
  name = models.CharField(max_length = 100)
  notes = models.TextField()
  resultURL = models.TextField()
  season = models.CharField(max_length = 10, choices = season_options)
  splitURL = models.TextField()

  def __str__(self):
    return self.name

class Result (models.Model):
  athlete = models.ForeignKey(Athlete, on_delete = models.DO_NOTHING)
  event = models.ForeignKey(Event, on_delete = models.DO_NOTHING)
  result = models.FloatField(null = False)
  distanceResult = models.BooleanField(default = False)

  def __str__(self):
    return self.result
