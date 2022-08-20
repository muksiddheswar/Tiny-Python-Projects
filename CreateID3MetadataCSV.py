import pandas as pd
import eyed3
from os import listdir, path

p = "D:\Multimedia\MZK\__new_indie_dwn\Indie dwn"

dfs = []

for f in listdir(p):
    if path.isfile(path.join(p, f)):
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


"""
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
print(df)
"""
