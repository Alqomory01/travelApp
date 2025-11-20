from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, LocationViewSet, MultiCitySegmentViewSet


router = DefaultRouter()
router.register('bookings', BookingViewSet, basename='bookings')
router.register('locations', LocationViewSet, basename='locations')
router.register('segments', MultiCitySegmentViewSet, basename='segments') 

urlpatterns = router.urls
