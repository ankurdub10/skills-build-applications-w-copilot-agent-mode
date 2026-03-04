from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router instance
router = DefaultRouter()

# Add your viewsets to router here
# router.register(r'activities', ActivityViewSet)
# router.register(r'users', UserViewSet)
# router.register(r'teams', TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
