'''
top_tracks_extractor gets the info of the top 10 tracks for every artist.
It generates a CSV file with the top 10 tracks of each artist.
'''

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from requests.exceptions import ReadTimeout

artists = pd.read_csv('./artists.csv')
artists = artists['ID'].to_dict()

# These are the Client ID and Client Secret needed to access the API. These are obtained in the 
# Spotify API web

cid = ''
secret = ''

# requests_timeout and retries parameters need to be changed to 10 to avoid timeouts from the API

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, requests_timeout=10, retries=10)

new_tracks = []

for artist_id in artists.values():
    try:
        top_tracks = sp.artist_top_tracks(artist_id)
    except ReadTimeout:
        top_tracks = sp.artist_top_tracks(artist_id)
    except:
        new_tracks.append(None)
    else:
        num_tracks = len(top_tracks['tracks'])
        for i in range(num_tracks):
            track_info = top_tracks['tracks'][i]
            new_track = {}
            new_track['track_id'] = track_info['id']
            new_track['name'] = track_info['name']
            new_track['artist_id'] = artist_id
            new_track['popularity'] = track_info['popularity']
            new_track['position'] = i # position is the index of the track in the top 10.
            new_tracks.append(new_track)

tracks_df = pd.DataFrame.from_records(new_tracks)

tracks_df.to_csv('./top_tracks.csv', index=False)
print('Top tracks CSV file created succesfully.')
