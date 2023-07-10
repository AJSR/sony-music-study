'''
artists_extractor is a script for the extraction of data of Sony Music artists from the Spotify API.
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

artists_df = pd.read_csv('./sony_artists.csv')

artists_dict = artists_df['Artist'].to_dict() # Convert to dictionary for performance reasons
artists_ids = []
artists_followers = []
artists_popularity = []
artists_list = []
missing_artists = []

for a in artists_dict.values():
    search_result = sp.search(q=f'artist:{a}', type='artist', limit=1)
    try:
        artist_id = search_result['artists']['items'][0]['id']
        artist_followers = sp.artist(artist_id)['followers']['total']
        artist_popularity = sp.artist(artist_id)['popularity']
    except ReadTimeout: # Sometimes the API timeouts for no reason, so this is needed to avoid it
        print(f'Timeout with artist {a}')
        artist_id = search_result['artists']['items'][0]['id']
    except:
        # if the artist can't be found insert it into the missing artists list
        artists_ids.append(None)
        artists_followers.append(None)
        artists_popularity.append(None)
        missing_artists.append(a)
    else:
        print(f'Inserting {a}')
        artists_ids.append(artist_id)
        artists_followers.append(artist_followers)
        artists_popularity.append(artist_popularity)


artists_df['ID'] = artists_ids
artists_df['Followers'] = artists_followers
artists_df['Popularity'] = artists_popularity

missing_df = artists_df[artists_df['ID'].isna()]['Artist']
missing_dict = missing_df.to_dict()

missing_df.to_csv('./missing_artists.csv', index=False)
print('Saved missing artists dataframe in "missing_artists.csv"')

artists_ready = artists_df.dropna()

artists_ready.to_csv('./artists.csv', index=False)

print(f'The number of artists not found in Spotify is {len(missing_dict)}')

print('The list of missing artists is:')
for a in missing_dict.values():
    print(a)
