# small script to count how many times albums/artists appear in playlists
# Usage: py sort_occurrences.py [Path to exported playlist YAML file] [album|artist]

import sys
from yaml import safe_load

if len(sys.argv) != 3 or sys.argv[2] not in ("album", "artist"):
    print("Usage: py sort_occurrences.py [Path to exported playlist YAML file] [album|artist]")
    sys.exit(1)
yaml_path, sort_by = sys.argv[1], sys.argv[2]

with open(yaml_path, encoding="utf-8") as f:
    playlist_dict = safe_load(f.read())

counts = {}
if sort_by == "album":
    for track in playlist_dict["pl_tracks"]:
        album_name = track["album"]["album_name"]
        if album_name in counts:
            counts[album_name] += 1
        else:
            counts[album_name] = 1
elif sort_by == "artist":
    for track in playlist_dict["pl_tracks"]:
        for artist in track["artists"]:
            artist_name = artist["artist_name"]
            if artist_name in counts:
                counts[artist_name] += 1
            else:
                counts[artist_name] = 1

sorted_counts = sorted(counts, key=counts.get)
for count in sorted_counts:
    print(f"{count}: {counts[count]}")