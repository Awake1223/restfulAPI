from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParentViewSet, ChildViewSet, ActivityViewSet

router = DefaultRouter()
router.register(r'parents', ParentViewSet)
router.register(r'children', ChildViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]