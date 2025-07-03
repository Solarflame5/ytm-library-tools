from yaml import dump

yaml_track_template = {
    "pl_title": "cool playlist",
    "pl_description": "description of cool playlist",
    "pl_author": "cooldude51",
    "pl_year": "2025",
    "pl_duration_str": "2 hours",
    "pl_duration_seconds": 7200,
    "pl_tracks": [
        {
            "title": "track 1",
            "artists": [
                {"artist_name": "unknown artist", "artist_id": "jdhfsgks"}
            ],
            "video_id": "sdfa",
            "album": {"album_title": "brainrot", "album_id": "fdfghljsdgh"}
        },
        {
            "title": "track 2",
            "artists": [
                {"artist_name": "unknown artist", "artist_id": "jdhfsgks"}
            ],
            "video_id": "dfsa",
            "album": {"album_title": "brainrot", "album_id": "fdfghljsdgh"}
        },
        {
            "title": "random music",
            "artists": [
                {"artist_name": "unknown artist", "artist_id": "jdhfsgks"}
            ],
            "video_id": "fdas",
            "album": {"album_title": "single", "album_id": "436346"}
        },
        {
            "title": "eeeeeeeeeee",
            "artists": [
                {"artist_name": "unknown artist", "artist_id": "jdhfsgks"}
            ],
            "video_id": "asfd",
            "album": {"album_title": "eeeeeeeeeeeeeeeeee", "album_id": "fd5345dgh"}
        }
    ]

}

print(dump(yaml_track_template, sort_keys=False))