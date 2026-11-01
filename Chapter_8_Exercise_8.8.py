print("\n=== 8-8. User Albums ===")
def make_album(artist, title, songs=None):
    """Bangun dictionary yang menggambarkan sebuah album musik."""
    album = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album['songs'] = songs
    return album
while True:
    print("\n(ketik 'quit' kapan saja untuk berhenti)")

    artist_name = input("Nama artis: ")
    if artist_name == 'quit':
        break

    album_title = input("Judul album: ")
    if album_title == 'quit':
        break

    album = make_album('Charlie Puth', 'Nine Track Mind')
    print(f"Album yang dibuat: {album}")