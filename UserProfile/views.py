from django.shortcuts import render
from UserProfile import serializers
from rest_framework import response, viewsets, status
from UserProfile.models import UserModel, UserProfileManager
from rest_framework.authentication import TokenAuthentication
from UserProfile import permissions
from rest_framework import filters #for search filters
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.settings import api_settings


# Create your views here.


class UserProfile(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'email']


class UserLoginAPIView(ObtainAuthToken):
    """ Handle creating user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


