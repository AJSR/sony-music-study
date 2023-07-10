'''
albums_extractor is a script that gets all the albums relevant information from the artists CSV file.
It generates a CSV file with the albums information redy to be used.
'''

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from requests.exceptions import ReadTimeout

# These are the Client ID and Client Secret needed to access the API. These are obtained in the 
# Spotify API web

cid = ''
secret = ''

# requests_timeout and retries parameters need to be changed to 10 to avoid timeouts from the API

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, requests_timeout=10, retries=10)

artists_df = pd.read_csv('./artists.csv')

artists_ids = artists_df['ID'].to_dict()

temp_list = []

# Get a dataframe with the albums and artists ids
for a in artists_ids.values():
    try:
        response = sp.artist_albums(a)
    except ReadTimeout:
        response = sp.artist_albums(a)
    except:
        (f'Something went wrong with artist {a}')
    else:
        total_albums = len(response['items'])
        for i in range(total_albums):
            album = response['items'][i]
            new_album = {}
            new_album['id'] = album['id']
            new_album['artist_id'] = a
            temp_list.append(new_album)

albums_df = pd.DataFrame.from_records(temp_list)

# albums_df might need to be saved if the whole script makes too many requests, so we can make 
# the first set of requests and save it and the second set of requests later when the API lets us. 

albums_ids = albums_df['id'].to_list()

# For complexity reasons, the API method used is GET SEVERAL ALBUMS (albums method in spotipy)
# so we can get 20 albums per request, reducing the number of requests to the API

len_albs = len(albums_ids)

st = 20 if len_albs % 20 == 0 else len_albs % 20
index = 0

album_type_list = []
album_name_list = []
album_release_list = []
album_label_list = []
album_popularity_list = []

for i in range(0, len_albs, st):
    try:
        response = sp.albums(albums_ids[index:index+st])
    except ReadTimeout:
        response = sp.albums(albums_ids[index:index+st])
    except:
        (f'Something went wrong')
    else:
        total_albums = len(response['albums'])
        for j in range(total_albums):
            album_info = response['albums'][j]
            album_type_list.append(album_info['type'])
            album_name_list.append(album_info['name'])
            album_release_list.append(album_info['release_date'])
            album_label_list.append(album_info['label'])
            album_popularity_list.append(album_info['popularity'])
            print(f'{album_info["name"]} inserted')
        
        index = index+st
        st = st = 20 if len_albs % 20 == 0 else len_albs % 20

albums_df['name'] = album_name_list
albums_df['type'] = album_type_list
albums_df['release_date'] = album_release_list
albums_df['label'] = album_label_list
albums_df['popularity'] = album_popularity_list

albums_df.to_csv('./albums.csv', index=False)

print('Albums CSV file created successfully.')
