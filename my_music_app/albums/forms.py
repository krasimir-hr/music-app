from django import forms

from my_music_app.albums.models import Album


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['name', 'artist', 'genre', 'description', 'image_url', 'price']

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Album Name'}
            ),

            'artist': forms.TextInput(
                attrs={'placeholder': 'Artist'}
            ),

            'description': forms.TextInput(
                attrs={'placeholder': 'Description'}
            ),

            'image_url': forms.TextInput(
                attrs={'placeholder': 'Image URL'}
            ),

            'price': forms.TextInput(
                attrs={'placeholder': 'Price'}
            ),

        }


class AlbumDeleteForm(AlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'