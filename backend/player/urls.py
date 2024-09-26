from django.urls import path
from . import views


urlpatterns = [
    path('song/', views.SongView.as_view(), name='song'),
    path('song/<int:id>/like/check/', views.ReactSong.as_view()),
    path('song/<int:id>/like-or-dislike/', views.ReactSong.as_view()),
    path('song/remove/<int:id>/', views.DeleteSong.as_view(), name='remove-song'),
    path('playlist/', views.PlaylistView.as_view(), name='playlist'),
]