from lists.lists import (
    separators,
    found_track_names,
    docs_track_names,
    lower_case_letters,
    extras_cap_variants,
)
from utils.string_utils import generate_potential_track_name_sections
from utils.file_utils import load_map, get_known_track_names
from utils.hash_utils import check_hash
import os

TRACKS_MAP_PATH = os.path.join(os.path.dirname(__file__), "maps/tracks_map.json")
TRACKS_MAP_NEW_PATH = os.path.join(
    os.path.dirname(__file__), "maps/tracks_map_new.json"
)

if __name__ == "__main__":
    map_json = load_map(TRACKS_MAP_NEW_PATH)

    known_track_names, known_track_hashes = get_known_track_names(map_json)

    result = check_hash("ER_output", known_track_hashes)

    print(f"Result: {result}")
