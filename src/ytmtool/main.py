import argparse
from collections import Counter
from pathlib import Path

from tabulate import tabulate

import ytmtool.fileops as fileops
import ytmtool.ytmops as ytmops


def handle_list(args):
    print(tabulate(ytmops.get_playlist_stubs(), headers=["Title", "ID", "Description", "Author"])) # type: ignore[reportArgumentType] # tabulate does support lists of dataclasses

def handle_export(args):
    return

def handle_stats(args):
    stat_type = args.type
    filepath = args.filepath

    playlist = fileops.read_playlist_from_file(filepath)
    if stat_type == "album":
        albums = []
        for track in playlist.tracks:
            if track.album is None:
                continue
            albums.append(f"{track.artists[0].name} - {track.album.title}")
        raw_counts = Counter(albums).most_common()
        truncated_counts = [] # TODO: convert into list comprehension
        for count in raw_counts:
            if count[1] == 1:
                continue
            truncated_counts.append(count)
        print(tabulate(truncated_counts, headers=["Album Title", "Count"]))
    elif stat_type == "artist":
        pass

def main():
    parser = argparse.ArgumentParser(
        prog = "ytmtool"
    )
    subparsers = parser.add_subparsers(required=True)

    list_parser = subparsers.add_parser("list", help="List playlists in library")
    list_parser.set_defaults(func=handle_list)

    export_parser = subparsers.add_parser("export", help="Export playlist(s) to JSON file(s)")
    export_parser.set_defaults(func=handle_export)

    stats_parser = subparsers.add_parser("stats", help="Show statistics from exported playlist")
    stats_parser.add_argument("type", choices=["album", "artist"], help="Type to count in playlist tracks")
    stats_parser.add_argument("filepath", type=Path, help="Path to playlist JSON file")
    stats_parser.set_defaults(func=handle_stats)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()