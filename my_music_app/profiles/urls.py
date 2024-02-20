from django.urls import path, include

from my_music_app.profiles import views


urlpatterns = [
    path('details/', views.ProfileDetailsView.as_view(),  name='profile-details'),
    path('delete/', views.DeleteProfileView.as_view(), name='delete-profile'),
]
