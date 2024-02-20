from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from my_music_app.albums.models import Album
from my_music_app.albums.forms import AlbumForm, AlbumDeleteForm
from my_music_app.profiles.models import Profile


class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.owner = Profile.objects.last()
        return super().form_valid(form) 


class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'albums/album-details.html'
    context_object_name = 'album'



class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album-edit.html'
    context_object_name = 'album'
    
    def get_success_url(self):
        return reverse_lazy('album-details', kwargs={'pk': self.object.id})


class DeleteAlbumView(DeleteView):
    model = Album
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home-page')

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AlbumDeleteForm(initial=self.object.__dict__)
        return context
    
    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        album.delete()
        return redirect(self.success_url)
