import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import random
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
emotifyPath = os.getenv("EMOTIFY_PATH")
print(client_id, client_secret,emotifyPath)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id,
                                               client_secret= client_secret,
                                               redirect_uri="http://localhost:8000",
                                               scope="user-read-playback-state streaming ugc-image-upload playlist-modify-public"))

df1 = pd.read_csv(emotifyPath+'\songRecommender\data\data_moods.csv')
fp=open(emotifyPath+r'\new.txt','r')
mood = fp.read()
fp.close()

df2 = df1.loc[df1['mood'] == mood]
df2 = df2.astype({'id':'string'})
list_of_songs=[]
for row in df2.iterrows():
    list_of_songs.append("spotify:track:"+str(row[1]['id']))
list_of_songs=random.sample(list_of_songs,15)
print(len(list_of_songs))
playlist_name = mood+' Songs'
playlist_description = mood+' Songs'
user_id = sp.me()['id']
sp.user_playlist_create(user=user_id,name=playlist_name,public=True,description=playlist_description)
prePlaylists = sp.user_playlists(user=user_id)
playlist = prePlaylists['items'][0]['id']
print(playlist)
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist, tracks=list(list_of_songs))
print("Created "+mood+" playlist")
fp=open(emotifyPath+r'\new.txt','w')
fp.write(playlist)
fp.close()
os.system('python '+emotifyPath+r'\songRecommender\test2.py')