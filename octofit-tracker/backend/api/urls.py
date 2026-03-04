from django.urls import path, include
from rest_framework.routers import DefaultRouter

# import viewsets so they can be registered with the router
from .views import (
    ActivityViewSet,
    UserViewSet,
    TeamViewSet,
    WorkoutViewSet,
    LeaderboardViewSet,
)

# Create a router instance
router = DefaultRouter()

# register the viewsets with route prefixes matching the models
router.register(r'activities', ActivityViewSet)
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboards', LeaderboardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
