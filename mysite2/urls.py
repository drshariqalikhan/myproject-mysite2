
from django.conf.urls import url,include
from django.contrib import admin
# from rest_framework.authtoken import views
from mysite2 import views

# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('myop_app.urls')),
]
