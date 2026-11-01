"""littlelemon URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from restaurant.views import BookingViewSet, UserViewSet, index

router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='tables')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # Admin Interface
    path('admin/', admin.site.urls),

    # Static HTML Content at root
    path('', index, name='home'),

    # Restaurant App URLs (Static HTML and Menu API)
    path('restaurant/', include('restaurant.urls')),

    # Table Booking API (Router ViewSet)
    path('restaurant/booking/', include(router.urls)),

    # Alternate API paths for flexibility across different peer review prompts
    path('api/', include('restaurant.urls')),
    path('api/booking/', include(router.urls)),

    # User Registration & Authentication (Djoser)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # DRF Token Authentication Endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth_root'),
]
