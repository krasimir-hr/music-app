from django.urls import path, include

from my_music_app.albums import views


urlpatterns = [
    path('add/', views.AddAlbumView.as_view(), name='add-album'),
    path('<int:pk>/', include ([
        path('details/', views.AlbumDetailsView.as_view(), name='album-details'),
        path('edit/', views.EditAlbumView.as_view(), name='edit-album'),
        path('delete/', views.DeleteAlbumView.as_view(), name='delete-album'),
    ]))
]
