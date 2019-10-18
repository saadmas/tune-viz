import pandas as pd
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

# APP SECRET MISSING FROM CLIENT CREDENTIALS INSTANTIATION
client_credentials_manager = SpotifyClientCredentials("a334b187376741b1bd1acf909bd989ae","")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

"""
NOTE: to get IDs of top tracks:
- sp.search("Track Name - Rezz")
- find track uri in result from search
"""

trackNames = ["Relax", "Lonely", "Flying Octopus", "Spider On The Moon", "Life & Death"]
trackIds = ['3oDXLJTEs6YX1gJD3aOsnZ', '1CLU9Dv75foPZSBvdXyWnD', '1gK4D83DSL023cYBsuhIQV', '4Ft6PIfruwhXypkAeT4S0u', '4bmvfx88H75CcEE0mKXD3q']
audioFeatures = sp.audio_features(trackIds)


dfColumns = ["Danceability", "Energy", "Instrumentalness", "Valence"]
dfRows = []

for af in audioFeatures:
    dfRows.append([af["danceability"], af["energy"], af["instrumentalness"], af["valence"]])

df = pd.DataFrame(index=trackNames, data=dfRows, columns=dfColumns)
df

dfDance = df["Danceability"]
ax = dfDance.plot(kind="bar", title="Danceability", yticks=[0, 0.5, 1], color="#1DB954")
ax.set_yticklabels(["No groove", "Kinda dancey", "Get on the floor!"])
ax

dfEnergy = df["Energy"]
ax = dfEnergy.plot(kind="bar", title="Energy", yticks=[0, 0.5, 1], color="#1DB954")
ax.set_yticklabels(["Falling asleep", "Gettin' loud", "CAN U HEAR DAT?"])
ax

dfInstrumentalness = df["Instrumentalness"]
ax = dfInstrumentalness.plot(kind="bar", title="Instrumentalness", yticks=[0, 0.5, 1], color="#1DB954")
ax.set_yticklabels(["Vocals galore", "Pretty instrumental", "No vocalz here!"])
ax

dfValence = df["Valence"]
ax = dfValence.plot(kind="bar", title="Valence", yticks=[0, 0.5, 1], color="#1DB954")
ax.set_yticklabels(["Sunken", "Some typa way", "Super happy!"])
ax