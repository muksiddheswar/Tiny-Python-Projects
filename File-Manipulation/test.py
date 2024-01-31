import pandas as pd

simple_list = ['01. Hyena Express - Shonar Bangla Circus.mp3',
               'Shonar Bangla Circus',
               '01. Hyena Express',
               None,
               None,
               None,
               None,
               None]

simple_list = ['None' if v is None else v for v in simple_list]
cols = ['Filename', 'Title', 'Artist', 'Album', 'Album_Artist', 'Composer', 'Publisher', 'Genre']


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
print(pd.DataFrame([simple_list], columns=cols))

