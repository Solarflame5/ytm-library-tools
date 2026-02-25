from os import getenv

from dotenv import load_dotenv
from ytmusicapi import OAuthCredentials, YTMusic

import ytmtool.models as models

__all__ = ["ytmusic", "get_playlist_stubs", "get_playlist"]

load_dotenv()
if (env_auth_type := getenv("AUTH_TYPE")) is not None:
    if env_auth_type == "browser":
        ytmusic = YTMusic("browser.json")
    elif env_auth_type == "oauth":
        env_client_id = getenv("CLIENT_ID")
        env_client_secret = getenv("CLIENT_SECRET")
        if env_client_id is None or env_client_secret is None:
            raise KeyError("OAuth2 credentials missing in environent")

        ytmusic = YTMusic(
            "oauth.json",
            oauth_credentials=OAuthCredentials(
                client_id=env_client_id,
                client_secret=env_client_secret
            )
        )
    else:
        raise KeyError("Incorrect authentication type in environment")
else:
    raise KeyError("Authentication type not set in environment")

def get_playlist_stubs() -> list[models.PlaylistStub]:
    raw_data = ytmusic.get_library_playlists(limit=None)
    stub_list = []
    for raw_playlist in raw_data:
        playlist_stub = models.PlaylistStub(
            title = raw_playlist["title"],
            id = raw_playlist["playlistId"],
            description = raw_playlist["description"],
            author = raw_playlist["author"][0]["name"] if raw_playlist.get("author") else None
        )
        stub_list.append(playlist_stub)
    return stub_list

def get_playlist(playlist_id: str) -> models.Playlist:
    raw_data = ytmusic.get_playlist(playlist_id, limit=None)
    tracks: list[models.Track] = []
    for raw_track in raw_data["tracks"]:
        artists = []
        for raw_artist in raw_track["artists"]:
            artist = models.Artist(
                name = raw_artist["name"],
                id = raw_artist["id"]
            )
            artists.append(artist)
        track = models.Track(
            title = raw_track["title"],
            id = raw_track.get("videoId"),
            artists = artists,
            album = models.Album(
                title = raw_track["album"]["name"],
                id = raw_track["album"]["id"]
            ) if raw_track["album"] is not None else None,
            video_type = raw_track.get("videoType"),
            duration_seconds = raw_track["duration_seconds"]
        )
        tracks.append(track)
    playlist = models.Playlist(
        title = raw_data["title"],
        author = raw_data["author"]["name"] if raw_data.get("author") else None,
        description = raw_data["description"],
        id = raw_data["id"],
        track_count = len(tracks),
        duration_str = raw_data["duration"],
        tracks = tracks
    )
    return playlist

# if __name__ == "__main__": # code for testing
#     pass