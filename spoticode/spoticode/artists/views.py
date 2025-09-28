from datetime import datetime
# Django
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# Project
from spoticode.artists.models import Artist, ArtistLink
from spoticode.artists.forms import CreateArtistForm, EditArtistForm, EditArtistLinkForm
from spoticode.web.access_validators import custom_login_required, can_create_or_update, can_delete, can_read, database_required
from spoticode.web.access_checkers import can_create_checker, can_edit_checker, can_delete_checker


@custom_login_required
@database_required
@can_read
def show_all_artists(request):
    artists = Artist.objects.all()
    query = request.GET.get('query')
    
    if query:
        artists = Artist.objects.filter(artist_name__icontains=query) | \
            Artist.objects.filter(other_names__icontains=query)
    
    artists = artists.order_by('artist_name')
    
    paginator = Paginator(artists, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'curr_year': datetime.now().year,
        'artists': artists,
        'total_artists': artists.count(),
        'page_obj': page_obj,
        'can_create_check': can_create_checker(request.user),
    }
    
    return render(request, 'artists/artists-all.html', context)


@custom_login_required
@database_required
@can_read
def show_details_artist(request, id):
    artist = get_object_or_404(Artist, id=id)
    artist_links = get_object_or_404(ArtistLink, for_artist=id)
    
    artist_fields = []
    for field_name in artist.__class__.field_order():
        field = artist._meta.get_field(field_name)
        artist_fields.append({
            'verbose_name': field.verbose_name.title(),
            'type': field.__class__.__name__,
            'value': getattr(artist, field.name),
        })
        
    links_fields = []
    for field_name in artist_links.__class__.field_order():
        field = artist_links._meta.get_field(field_name)
        links_fields.append({
            'verbose_name': field.verbose_name.title(),
            'type': field.__class__.__name__,
            'value': getattr(artist_links, field.name),
        })
    
    context = {
        'curr_year': datetime.now().year,
        'artist': artist,
        'artist_fields': artist_fields,
        'links_fields': links_fields,
        'can_edit_check': can_edit_checker(request.user),
        'can_delete_check': can_delete_checker(request.user),
    }
    
    return render(request, 'artists/artist-details.html', context)


@custom_login_required
@database_required
@can_create_or_update
def create_artist(request):
    form = CreateArtistForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        artist = form.save()
        return redirect('artist_details', id=artist.id)

    context = {
        'curr_year': datetime.now().year,
        'form': form,
    }

    return render(request, 'artists/artist-create.html', context)


@custom_login_required
@database_required
@can_create_or_update
def edit_artist_info(request, id):
    artist = get_object_or_404(Artist, id=id)
    form = EditArtistForm(request.POST or None, instance=artist)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('artist_details', id=artist.id)
    
    context = {
        'curr_year': datetime.now().year,
        'artist': artist,
        'form': form,
    }
    
    return render(request, 'artists/artist-info-edit.html', context)


@custom_login_required
@database_required
@can_create_or_update
def edit_artist_links(request, id):
    artist = get_object_or_404(Artist, id=id)
    artist_links = get_object_or_404(ArtistLink, for_artist=id)
    form = EditArtistLinkForm(request.POST or None, instance=artist_links)
    
    if request.method == 'POST' and form.is_valid():
        
        spotify_link = form.cleaned_data['spotify_link']
        if spotify_link and '?si=' in spotify_link:
            spotify_link = spotify_link.split('?si=')[0]
            artist_links.spotify_link = spotify_link
        
        wiki_curid = form.cleaned_data['wiki_curid']
        if wiki_curid:
            wiki_link = f'https://en.wikipedia.org/?curid={wiki_curid}'
            artist_links.wikipedia_link = wiki_link
        elif not wiki_curid:
            artist_links.wikipedia_link = None
        
        form.save()
        return redirect('artist_details', id=artist.id)
    
    context = {
        'curr_year': datetime.now().year,
        'artist_links': artist_links,
        'form': form,
        'artist': artist,
    }
    
    return render(request, 'artists/artist-links-edit.html', context)


@custom_login_required
@database_required
@can_delete
def delete_artist(request, id):
    artist = get_object_or_404(Artist, id=id)
    
    if request.method == 'POST':
        artist.delete()
        return redirect('artists_all')

    context = {
        'curr_year': datetime.now().year,
        'artist': artist,
    }
    
    return render(request, 'artists/artist-delete.html', context)
