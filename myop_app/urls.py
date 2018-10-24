from django.conf.urls import url
from . import views
from .views import GetUpClassView,MedPicClassView,PreopClassView,DashView,LoginView
from django.contrib.auth.views import (
    login,
    logout,
    # password_reset,
    # password_reset_done,
    # password_reset_confirm,
    # password_reset_complete
    )
app_name = 'myop_app'

urlpatterns = [
    url(r'^dash/',views.index),
    url(r'^add/jd/$',views.add_jd, name ="add_jd"),
    url(r'^edit/jd/(?P<id>\d+)/$',views.edit_jd,name ="edit_jd"),
    url(r'^alert/$',views.alert, name ="alert"),

    url(r'^register/$',views.register, name = 'register'),
    url(r'^$', login, {'template_name':'myop_app/login.html'}),
    url(r'^logout/$', logout, {'template_name':'myop_app/logout.html'}),


    url(r'^auth/login/',LoginView.as_view()),

    url(r'^connect/',GetUpClassView.as_view()),
    url(r'^medpic/',MedPicClassView.as_view()),
    url(r'^preop/',PreopClassView.as_view()),
    url(r'^db/',DashView.as_view()),

]