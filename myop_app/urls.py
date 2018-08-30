from django.conf.urls import url
from . import views
from .views import GetUpClassView,MedPicClassView,PreopClassView,DashView
urlpatterns = [
    url(r'^connect/',GetUpClassView.as_view()),
    url(r'^medpic/',MedPicClassView.as_view()),
    url(r'^preop/',PreopClassView.as_view()),
    url(r'^db/',DashView.as_view()),
    url(r'^dash/',views.index),
    url(r'^register/$',views.register),
]