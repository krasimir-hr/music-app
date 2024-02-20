from django.urls import path, include

from my_music_app.common import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home-page'),
]
