from rest_framework import viewsets, permissions
from .models import Booking, MultiCitySegment, Location
from .serializers import BookingSerializer, MultiCitySegmentSerializer, LocationSerializer
from .permissions import IsAdminOrOwner
# from rest_framework.authentication import TokenAuthentication


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self): 

        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()
        
        user = self.request.user

        if not user.is_authenticated:
            return Booking.objects.none()
        
        role = getattr(user, "role", None)

        if role == "admin":
            return Booking.objects.all()

        if role == "agent":
            return Booking.objects.filter(agent=user)
     
        return Booking.objects.filter(customer=user)

    def perform_create(self, serializer):
        serializer.save()

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class MultiCitySegmentViewSet(viewsets.ModelViewSet):
    queryset = MultiCitySegment.objects.all()
    serializer_class = MultiCitySegmentSerializer
    permission_classes = [permissions.IsAuthenticated]
