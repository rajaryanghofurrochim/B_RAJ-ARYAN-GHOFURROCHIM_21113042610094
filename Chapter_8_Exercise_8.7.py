def make_album(artist, title, songs=None):
    """Bangun dictionary yang menggambarkan sebuah album musik."""
    album = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album['songs'] = songs
    return album


print("\n=== 8-7. Album ===")
print(make_album('queen', 'a night at the opera'))
print(make_album('nirvana', 'nevermind'))
print(make_album('coldplay', 'parachutes'))
print(make_album('adele', '21', songs=11))      