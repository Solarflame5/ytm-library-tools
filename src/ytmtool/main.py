import argparse


def handle_list():
    return

def handle_export():
    return

def handle_stats():
    return

def main():
    parser = argparse.ArgumentParser(
        prog = "ytmtool"
    )
    subparsers = parser.add_subparsers()

    list_parser = subparsers.add_parser("list", help="List playlists in library")

    export_parser = subparsers.add_parser("export", help="Export playlist(s) to JSON file(s)")

    stats_parser = subparsers.add_parser("stats", help="Show statistics from exported playlist")

    args = parser.parse_args()

if __name__ == "__main__":
    main()