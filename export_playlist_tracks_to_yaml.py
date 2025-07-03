"""
This script exports a list of tracks from a given playlist to a timestamped TSV file under ./output/

$ py export_playlist_tracks_to_tsv.py [PLAYLIST ID]

output/2025-01-01 13.00.00 - Liked Music.yml
    
"""

yaml_track_template = {
    "pl_title": "",
    "pl_description": "",
    "pl_author": "",
    "pl_year": "",
    "pl_duration_str": "",
    "pl_duration_seconds": 0,
    "pl_tracks": [
        {
            "title": "",
            "artists": [
                {"artist_name": "", "artist_id": ""}
            ],
            "video_id": "",
            "album": {"album_title": "", "album_id": ""}
        }
    ]

}

import datetime
from pathlib import Path
from yaml import dump

from ytmusicapi import YTMusic
ytmusic = YTMusic("browser.json")

timestamp = datetime.datetime.now().replace(microsecond=0).isoformat(" ").replace(":", ".")
output_path = Path(__file__).parent / "output"
output_path.mkdir(parents=True, exist_ok=True)

playlist_id = "LM"

playlist = ytmusic.get_playlist(playlist_id, None)

output_dict = {
    "pl_title": playlist["title"],
    "pl_description": playlist["description"],
    "pl_author": "",
    "pl_year": playlist["year"],
    "pl_duration_seconds": playlist["duration_seconds"],
    "pl_tracks": []
}
try:
    output_dict["pl_author"] = playlist["author"]
except:
    output_dict["pl_author"] = "-Unknown-"

for track in playlist["tracks"]:
    tracks_dict = {
        "title": track["title"],
        "artists": [],
        "video_id": track["videoId"],
        "album": {}
    }
    try:
        tracks_dict["album"] = {"album_name": track["album"]["name"], "album_id": track["album"]["id"]}
    except:
        tracks_dict["album"] = {"album_name": "-Unknown-", "album_id": "-Unknown-"}

    for artist in track["artists"]:
        tracks_dict["artists"].append(
            {"artist_name": artist["name"], "artist_id": artist["id"]}
        )
    output_dict["pl_tracks"].append(tracks_dict)