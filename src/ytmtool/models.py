from dataclasses import dataclass


@dataclass
class Artist:
    name: str
    id: str

@dataclass
class Album:
    title: str
    id: str

@dataclass
class Track:
    title: str
    id: str
    album: Album | None
    artists: list[Artist]
    video_type: str
    duration_seconds: int

@dataclass
class PlaylistStub:
    title: str
    id: str
    description: str
    author: str | None

@dataclass
class Playlist:
    title: str
    author: str | None
    description: str
    id: str
    track_count: int
    duration_str: str
    tracks: list[Track]