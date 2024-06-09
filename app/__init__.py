import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "client_idを入力"
client_secret = "client_secretを入力"

def main():
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    track = sp.track('spotify:track:4cluDES4hQEUhmXj6TXkSo')
    print(track)

if __name__ == "__main__":
    main()