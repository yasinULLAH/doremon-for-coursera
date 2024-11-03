
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, TableBookingViewSet

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet)
router.register(r'bookings', TableBookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
