from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
  url(r'^athletes/$', views.AthleteGETAll.as_view()),
  url(r'^athletes/getAthlete/(?P<pk>[0-9]+)/$', views.AthleteGET.as_view()),
  url(r'^athletes/newAthlete/$', views.AthletePOST.as_view()),
  url(r'^athletes/updateAthlete/(?P<pk>[0-9]+)/$', views.AthletePUT.as_view()),
  url(r'^athletes/deleteAthlete/(?P<pk>[0-9]+)/$', views.AthleteDELETE.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
