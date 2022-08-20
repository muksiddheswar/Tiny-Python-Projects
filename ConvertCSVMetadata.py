import eyed3

audiofile = eyed3.load("pink.mp3")

print("Title:", audiofile.tag.title)
print("Artist:", audiofile.tag.artist)
print("Album:", audiofile.tag.album)
print("Album artist:", audiofile.tag.album_artist)
print("Composer:", audiofile.tag.composer)
print("Publisher:", audiofile.tag.publisher)
print("Genre:", audiofile.tag.genre)
