from django.urls import path, include
from rest_framework import routers
from UserProfile import views  

router = routers.DefaultRouter()
router.register(r'profile', views.UserProfile)
router.register(r'feed', views.UserProfileViewSet)

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls)),
    

]