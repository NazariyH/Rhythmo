from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.OwnProfileView.as_view(), name='own-profile'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/subscribe-or-unsubscribe/', views.ProfileView.as_view()),
    path('api/token-auth/', views.CustomAuthToken.as_view(), name='token_auth'),

]