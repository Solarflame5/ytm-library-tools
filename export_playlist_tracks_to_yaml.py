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

from ytmusicapi import YTMusic
ytmusic = YTMusic("browser.json")

timestamp = datetime.datetime.now().replace(microsecond=0).isoformat(" ").replace(":", ".")
output_path = Path(__file__).parent / "output"
output_path.mkdir(parents=True, exist_ok=True)

playlist_id = "LM"

playlist = ytmusic.get_playlist()