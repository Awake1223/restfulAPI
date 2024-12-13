from rest_framework import viewsets
from .models import Parent, Child, Activity
from .serializers import ParentSerializer, ChildSerializer, ActivitySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


#@api_view(['GET'])
@permission_classes([IsAuthenticated])
class ParentViewSet(viewsets.ModelViewSet):
    AuthPermission = [IsAuthenticated]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer



