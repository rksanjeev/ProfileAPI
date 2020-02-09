from django.shortcuts import render
from UserProfile import serializers
from rest_framework import response, viewsets, status
from UserProfile.models import UserModel, UserProfileManager, ProfileFeed
from rest_framework.authentication import TokenAuthentication
from UserProfile import permissions
from rest_framework import filters  # for search filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


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


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileFeedSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = ProfileFeed.objects.all()
    permission_classes = (permissions.UpdateStatus, IsAuthenticated)
    # IsAuthenticatedOrReadOnly will not allow anonymous user to send POST request thus making the app read-only
    # This behaviour can be changed to make it completely private and thus only authentivated user can read the write the app
    # using IsAuthenticated permission.

    def perform_create(self, serializer):
        """Must Override:: customized to get user from authenticated user """
        serializer.save(user=self.request.user)
