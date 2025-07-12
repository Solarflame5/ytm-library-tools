"""
This script exports a list of tracks from a given playlist to a timestamped YAML file under ./output/

$ py export_playlist_tracks_to_yaml.py --playlist [playlist id]
OR
$ py export_playlist_tracks_to_yaml.py --bulk [TSV or text file with playlist IDs seperated by newline]

output/2025-01-01 13.00.00 - [Playlist Name].yaml
    
"""

from yaml import dump
import time 

import argparse
argparser = argparse.ArgumentParser()
argparser.add_argument("-p", "--playlist")
argparser.add_argument("-b", "--bulk")
args = argparser.parse_args()

import datetime
timestamp = datetime.datetime.now().replace(microsecond=0).isoformat(" ").replace(":", ".")

from pathlib import Path
output_path = Path(__file__).parent / "output"
output_path.mkdir(parents=True, exist_ok=True)

from ytmusicapi import YTMusic
ytmusic = YTMusic("browser.json")

def get_playlist_dictionary(playlist_id: str) -> dict: 
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

    return output_dict

def export_dictionary_to_yaml(export_path: Path, playlist_dictionary: dict):
    with open(f"{export_path}/{timestamp} - {escape_filename(playlist_dictionary["pl_title"])}.yaml", "w", encoding="utf-8") as f:
        f.write(dump(playlist_dictionary, sort_keys=False, allow_unicode=True))

def escape_filename(input_str: str) -> str:
    output_str = input_str
    output_str = output_str.replace("/", "(slash)")
    output_str = output_str.replace("\\", "(bslash)")
    output_str = output_str.replace(":", "(colon)")
    output_str = output_str.replace("*", "(asterisk)")
    output_str = output_str.replace("?", "(qmark)")
    output_str = output_str.replace("\"", "(quote)")
    output_str = output_str.replace("<", "(lessthan)")
    output_str = output_str.replace(">", "(greaterthan)")
    output_str = output_str.replace("|", "(pipe)")
    return output_str

if not args.playlist == None and not args.bulk == None:
    print("You can only use one argument at once")
elif args.playlist == None and args.bulk == None:
    print("""Usage:
-p [Playlist ID] # Export a single playlist
-b [TSV or text file with playlist IDs seperated by newline] # Bulk export multiple playlists""")
elif not args.playlist == None:
    print("Starting export...")
    playlist_dictionary = get_playlist_dictionary(args.playlist)
    export_dictionary_to_yaml(output_path, playlist_dictionary)
    print(f"Playlist {playlist_dictionary["pl_title"]} has successfully been exported.")

elif not args.bulk == None:
    bulk_output_path = output_path / f"{timestamp} - Bulk Export"
    bulk_output_path.mkdir(parents=True, exist_ok=True)
    
    bulk_playlists_list = []
    with open(args.bulk, "r", encoding="utf-8") as f:
        for line in f.read().splitlines():
            bulk_playlists_list.append(line.split("\t")[0])
    
    print("Starting bulk export...")
    for playlist_id in bulk_playlists_list:
        playlist_dictionary = get_playlist_dictionary(playlist_id)
        export_dictionary_to_yaml(bulk_output_path, playlist_dictionary)
        print(f"Playlist \"{(playlist_dictionary["pl_title"])}\" has successfully been exported.")
        time.sleep(1)
    print("Bulk export successful!")
