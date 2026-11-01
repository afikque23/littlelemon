from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # Static HTML Content View
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    # Menu API Endpoints
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),

    # Direct Token Auth Endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
