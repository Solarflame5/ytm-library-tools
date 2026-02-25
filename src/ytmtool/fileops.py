import datetime
import json
import re
import unicodedata
from dataclasses import asdict
from pathlib import Path

import ytmtool.models as models

__all__ = ["get_iso_timestamp", "normalize_filename", "save_playlist_to_file", "read_playlist_from_file"]

def get_iso_timestamp() -> str:
    return (
        datetime.datetime.now()
        .replace(microsecond=0)
        .isoformat(" ")
        .replace(":", ".")
    )

def normalize_filename(raw_str: str) -> str:
    regexpattern = r"[^\w\ \_\-\[\]\(\)\,\.]"
    normalized = unicodedata.normalize("NFC", raw_str)
    normalized = re.sub(regexpattern, "_", normalized)
    normalized = normalized.strip(". ")
    return normalized

def save_playlist_to_file(playlist: models.Playlist, filepath: Path):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with filepath.open(mode="w", encoding="utf-8") as f:
        json.dump(asdict(playlist), f, indent=2, ensure_ascii=False)

def read_playlist_from_file(filepath: Path) -> models.Playlist:
    with filepath.open(encoding="utf-8") as f:
        raw_json = json.load(f)

    tracks = []
    for raw_track in raw_json["tracks"]:
        artists = []
        for raw_artist in raw_track["artists"]:
            artist = models.Artist(
                name = raw_artist["name"],
                id = raw_artist["id"]
            )
            artists.append(artist)
        track = models.Track(
            title = raw_track["title"],
            id = raw_track["id"],
            album = models.Album(
                title = raw_track["album"]["title"],
                id = raw_track["album"]["id"]
            ) if raw_track["album"] is not None else None,
            artists = artists,
            video_type = raw_track["video_type"],
            duration_seconds = raw_track["duration_seconds"]
        )
        tracks.append(track)

    playlist = models.Playlist(
        title = raw_json["title"],
        author = raw_json["author"],
        description = raw_json["description"],
        id = raw_json["id"],
        track_count = raw_json["track_count"],
        duration_str = raw_json["duration_str"],
        tracks = tracks
    )
    return playlist

# if __name__ == "__main__": # code for testing
#     pass