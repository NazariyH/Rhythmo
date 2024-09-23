from django.urls import path
from . import views


urlpatterns = [
    path('song/', views.SongView.as_view(), name='song'),
]