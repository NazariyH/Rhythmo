from django.urls import path
from . import views


urlpatterns = [
    path('song/', views.SongView.as_view(), name='song'),
    path('song/remove/<int:id>/', views.DeleteSong.as_view(), name='remove-song'),
]