from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework.response import Response
from rest_framework.decorators import api_view

router = routers.DefaultRouter()
# Register your viewsets here, e.g.:
# router.register(r'users', views.UserViewSet)

@api_view(['GET'])
def api_root(request):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('api/', include(router.urls)),
]
