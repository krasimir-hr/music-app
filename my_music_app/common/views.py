from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, RedirectView, TemplateView, CreateView

from my_music_app.albums.models import Album
from my_music_app.profiles.models import Profile
from my_music_app.profiles.forms import ProfileForm



class HomeView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not Profile.objects.exists():
            return NonAuthenticatedHomeView.as_view()(request, *args, **kwargs)
        else:
            return AuthenticatedHomeView.as_view()(request, *args, **kwargs)


class AuthenticatedHomeView(ListView):
    model = Album
    template_name = 'common/home-with-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_albums'] = Album.objects.all() 
        return context
    


class NonAuthenticatedHomeView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'common/home-no-profile.html'
    success_url = reverse_lazy('home-page')
