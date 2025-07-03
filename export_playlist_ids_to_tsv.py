"""
This script will save a list of playlists in your library to a timestamped TSV file under ./output/
Example:
    output/2025-01-01 13.00.00 - Playlist IDs.tsv
        Playlist ID	 Title	Author
        LM	Liked Music  -Unknown-
        PL4YL15T1D  Cool Music  You
        PL4YL15T1D  Uncool Music  You
        PL4YL15T1D  community playlist  cooldude51
"""

import datetime
from pathlib import Path

from ytmusicapi import YTMusic
ytmusic = YTMusic("browser.json")

timestamp = datetime.datetime.now().replace(microsecond=0).isoformat(" ").replace(":", ".")
output_path = Path(__file__).parent / "output"
output_path.mkdir(parents=True, exist_ok=True)

ytm_user_playlists = ytmusic.get_library_playlists(None)

with open(f"{output_path}/{timestamp} - Playlist IDs.tsv", "w", encoding="utf-8") as f:
    f.write("Playlist ID\tTitle\tAuthor\n")
    for playlist in ytm_user_playlists:
        try:
            playlist_author = playlist["author"][0]["name"]
        except:
            playlist_author = "-Unknown-"
        f.write(f"{playlist["playlistId"]}\t{playlist["title"]}\t{playlist_author}\n")