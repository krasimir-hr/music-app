from django import forms

from my_music_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Username'}
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email'}
            ),
            'age': forms.TextInput(
                attrs={'placeholder': 'Age'}
            ),
        }
