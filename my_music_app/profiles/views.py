from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView 

from my_music_app.profiles.models import Profile

class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return Profile.objects.last()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["album_count"] = self.object.album_set.count()
        return context
    

class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return Profile.objects.last()