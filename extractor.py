import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from requests.exceptions import ReadTimeout

cid = '5e40aa8e51864f7c86f0ee9481dbe45b'
secret = '8d25a2e13be542cb89a2daca2dcaab2b'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, requests_timeout=10, retries=10)

artists_df = pd.read_csv('./sony_artists.csv')

artists_dict = artists_df['Artist'].to_dict()
artists_ids = []

for a in artists_dict.values():
    search_result = sp.search(q=f'artist:{a}', type='artist', limit=1)
    try:
        artist_id = search_result['artists']['items'][0]['id']
    except ReadTimeout:
        artist_id = search_result['artists']['items'][0]['id']
    except:
        artists_ids.append('na')
    else:
        artists_ids.append(artist_id)

artists_df['ID'] = artists_ids

artists_df.to_csv('./artists.csv', index=False)
