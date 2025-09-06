from django import forms
# Project
from spoticode.songs.models import Song, SongLink, PendingSong
from spoticode.playlists.models import Playlist


# Songs
class CreateSongForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ('song_id', )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['song_title'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['main_artist'].widget.attrs.update({'class': 'form-select mb-3'})
        self.fields['feat_artist'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['genre_id'].widget.attrs.update({'class': 'form-select mb-3'})
        self.fields['song_year'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'YYYY'})
        self.fields['group_id'].widget.attrs.update({'class': 'form-select mb-3'})
        self.fields['album_id'].widget.attrs.update({'class': 'form-select mb-4'})


class EditSongForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ('song_id', )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['song_title'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['main_artist'].widget.attrs.update({'class': 'form-select mb-3'})
        self.fields['feat_artist'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['genre_id'].widget.attrs.update({'class': 'form-select mb-3'})
        self.fields['song_year'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'YYYY'})
        self.fields['group_id'].widget.attrs.update({'class': 'form-select mb-3'})
        self.fields['album_id'].widget.attrs.update({'class': 'form-select mb-4'})


class EditSongLinkForm(forms.ModelForm):
    wiki_curid = forms.CharField(label='Wikipedia ID', required=False)

    class Meta:
        model = SongLink
        fields = ('youtube_video_link', 'youtube_audio_link', 'spotify_link', 'wiki_curid', 'rateyourmusic_link')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['youtube_video_link'].widget.attrs.update({'class': 'form-control mb-3','placeholder': 'https://www.youtube.com/watch?v=...'})
        self.fields['youtube_audio_link'].widget.attrs.update({'class': 'form-control mb-3','placeholder': 'https://www.youtube.com/watch?v=...'})
        self.fields['spotify_link'].widget.attrs.update({'class': 'form-control mb-3','placeholder': 'https://open.spotify.com/track/...'})
        self.fields['wiki_curid'].widget.attrs.update({'class': 'form-control mb-3','placeholder': '123...'})
        self.fields['rateyourmusic_link'].widget.attrs.update({'class': 'form-control mb-4','placeholder': 'https://rateyourmusic.com/song/...'})
        
        if self.instance and self.instance.wikipedia_link:
            self.initial['wiki_curid'] = self.instance.wikipedia_link.split('=')[1]
        
    def clean(self):
        cleaned_data = super().clean()
        youtube_video_link = cleaned_data.get('youtube_video_link')
        youtube_audio_link = cleaned_data.get('youtube_audio_link')
        spotify_link = cleaned_data.get('spotify_link')
        wiki_curid = cleaned_data.get("wiki_curid")
        rateyourmusic_link = cleaned_data.get('rateyourmusic_link')

        if not youtube_video_link:
            self.cleaned_data['youtube_video_link'] = None
        if not youtube_audio_link:
            self.cleaned_data['youtube_audio_link'] = None
        if not spotify_link:
            self.cleaned_data['spotify_link'] = None
        if not wiki_curid:
            self.cleaned_data['wiki_curid'] = None
            self.cleaned_data['wikipedia_link'] = None
        if not rateyourmusic_link:
            self.cleaned_data['rateyourmusic_link'] = None

        return cleaned_data


class AddSongToPlaylistForm(forms.Form):
    playlist = forms.ModelChoiceField(queryset=Playlist.objects.all(), label='Select Playlist')
    
    def __init__(self, *args, **kwargs):
        song_id = kwargs.pop('id', None)
        super().__init__(*args, **kwargs)
        self.fields['playlist'].widget.attrs.update({'class': 'form-select mb-4'})
        
        if song_id:
            self.fields['playlist'].queryset = Playlist.objects.exclude(songplaylistrelation__song_id=song_id)



# Pending Songs
class CreatePendingSongForm(forms.ModelForm):
    class Meta:
        model = PendingSong
        fields = ('song_title', 'main_artist', 'feat_artist', 'to_group')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['song_title'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['main_artist'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['feat_artist'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['to_group'].widget.attrs.update({'class': 'form-select mb-4'})


class EditPendingSongForm(forms.ModelForm):
    class Meta:
        model = PendingSong
        fields = ('song_title', 'main_artist', 'feat_artist', 'to_group')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['song_title'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['main_artist'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['feat_artist'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['to_group'].widget.attrs.update({'class': 'form-select mb-4'})
