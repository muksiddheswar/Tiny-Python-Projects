# Read all .mp3 files in a location and creates a csv file of the id3 metadata.

import pandas as pd
import eyed3
from os import listdir, path

f = open("music_library_location.txt", "r")
p = f.read()

dfs = []

for f in listdir(p):
    if path.isfile(path.join(p, f)) and (f[-4:]).lower() == ".mp3":
        audiofile = eyed3.load(path.join(p, f))

        simple_list = [f,
                       audiofile.tag.title,
                       audiofile.tag.artist,
                       audiofile.tag.album,
                       audiofile.tag.album_artist,
                       audiofile.tag.composer,
                       audiofile.tag.publisher,
                       audiofile.tag.genre]
        simple_list = ['None' if v is None else v for v in simple_list]
        dfs.append(simple_list)

cols = ['Filename', 'Title', 'Artist', 'Album', 'Album_Artist', 'Composer', 'Publisher', 'Genre']
df = pd.DataFrame(dfs, columns=cols)
df.to_csv('out.csv')
