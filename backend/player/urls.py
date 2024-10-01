from django.urls import path
from . import views


urlpatterns = [
    path('song/', views.SongView.as_view(), name='song'),
    path('song/<int:id>/like/check/', views.ReactSong.as_view()),
    path('song/<int:id>/like-or-dislike/', views.ReactSong.as_view()),
    path('song/remove/<int:id>/', views.DeleteSong.as_view(), name='remove-song'),
    path('song/<int:id>/download/', views.downloadSong, name='download-song'),

    path('playlist/', views.PlaylistView.as_view(), name='playlist'),
    path('playlist/names/', views.PlaylistManagmentAPIView.as_view(), name='get-playlists-names'),
    path('playlist/song/<int:id>/add/', views.PlaylistManagmentAPIView.as_view(), name='add-song-to-playlist'),
    path('playlist/<int:id>/like/check/', views.ReactPlaylist.as_view()),
    path('playlist/<int:id>/like-or-dislike/', views.ReactPlaylist.as_view()),
    path('playlist/<int:id>/remove/', views.DeletePlaylist.as_view(), name='remove-playlist'),
    path('playlist/<int:id>/detail/', views.PlaylistDetailView.as_view(), name='playlist-detail'),
    path('playlist/<int:playlist_id>/song/<int:song_id>/remove/', views.RemoveSongFromPlaylist.as_view(), name='remove-song-from-playlist'),

    path('search/', views.SearchDataAPIView.as_view(), name='search'),
]