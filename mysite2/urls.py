
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.authtoken import views
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# /login -> POST login with 'username' and 'password' ; returns 'key' token
# /logout ->POST
#/user/ -> gets logged in user details

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('rest_auth.urls')),# to manage the login/logout
   url(r'^log/', views.obtain_auth_token, name='get_auth_token'),
    #TODO: urls to manage:
    #   1. get logged in user's journey data
    url(r'^api/', include('myop_app.urls')),
    #   2. update logged in user's journey data


    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
