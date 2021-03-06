from django.conf.urls import url
from django.contrib.auth import views as django_views

from rest_framework.urlpatterns import format_suffix_patterns

from app import views

urlpatterns = [
  url(r'^$', views.api_root),

  url(r'^athletes/$', views.AthleteGETAll.as_view()),
  url(r'^athletes/getAthlete/(?P<pk>[0-9]+)/$', views.AthleteGET.as_view()),
  url(r'^athletes/newAthlete/$', views.AthletePOST.as_view()),
  url(r'^athletes/updateAthlete/(?P<pk>[0-9]+)/$', views.AthletePUT.as_view()),
  url(r'^athletes/deleteAthlete/(?P<pk>[0-9]+)/$', views.AthleteDELETE.as_view()),

  url(r'^athletes/getAthleteResults/(?P<pk>[0-9]+)/$', views.GETAthletePerformances),
  url(r'^athletes/getAthleteBests/(?P<pk>[0-9]+)/$', views.GETAthleteBestPerformances),

  url(r'^events/$', views.EventGETAll.as_view()),
  url(r'^events/getEvent/(?P<pk>[0-9]+)/$', views.EventGET.as_view()),
  url(r'^events/newEvent/$', views.EventPOST.as_view()),
  url(r'^events/updateEvent/(?P<pk>[0-9]+)/$', views.EventPUT.as_view()),
  url(r'^events/deleteEvent/(?P<pk>[0-9]+)/$', views.EventDELETE.as_view()),

  url(r'^events/getTopPerformances/(?P<pk>[0-9]+)/$', views.GETEventTopPerformance),
  url(r'^events/getTopPerformances/$', views.GETEventTopPerformances),

  url(r'^events/getRecords/(?P<pk>[0-9]+)/$', views.GETRecord),
  url(r'^events/getRecords/$', views.GETRecords),

  url(r'^meets/$', views.MeetGETAll.as_view()),
  url(r'^meets/getMeet/(?P<pk>[0-9]+)/$', views.MeetGET.as_view()),
  url(r'^meets/newMeet/$', views.MeetPOST.as_view()),
  url(r'^meets/updateMeet/(?P<pk>[0-9]+)/$', views.MeetPUT.as_view()),
  url(r'^meets/deleteMeet/(?P<pk>[0-9]+)/$', views.MeetDELETE.as_view()),

  url(r'^results/$', views.ResultGETAll.as_view()),
  url(r'^results/getResult/(?P<pk>[0-9]+)/$', views.ResultGET.as_view()),
  url(r'^results/newResult/$', views.ResultPOST.as_view()),
  url(r'^results/updateResult/(?P<pk>[0-9]+)/$', views.ResultPUT.as_view()),
  url(r'^results/deleteResult/(?P<pk>[0-9]+)/$', views.ResultDELETE.as_view()),

  url(r'^news/$', views.NewsGETAll.as_view()),
  url(r'^news/getNews/(?P<pk>[0-9]+)/$', views.NewsGET.as_view()),
  url(r'^news/newNews/$', views.NewsPOST.as_view()),
  url(r'^news/updateNews/(?P<pk>[0-9]+)/$', views.NewsPUT.as_view()),
  url(r'^news/deleteNews/(?P<pk>[0-9]+)/$', views.NewsDELETE.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
