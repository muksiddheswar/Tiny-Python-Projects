import os
import csv
from datetime import datetime

path = '/'
path = os.path.abspath(path)

with open('Output-File.txt', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['identifier', 'file', 'description', 'subject[0]', 'title', 'creator', 'date', 'collection'])
    for root, dirs, files in os.walk(path):
        for filename in files:
            writer.writerow(['XXX', os.path.join(root, filename), '', '', filename, 'opensource',
                             datetime.today().strftime('%Y-%m-%d'), ''])
