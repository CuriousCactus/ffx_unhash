from lists.lists import (
    separators,
    found_track_names,
    docs_track_names,
    lower_case_letters,
    extras_cap_variants,
)
from utils.string_utils import generate_potential_track_name_sections
from utils.file_utils import load_map, get_known_track_names
from utils.hash_utils import search_for_known_hashes
import os

TRACKS_MAP_PATH = os.path.join(os.path.dirname(__file__), "maps/tracks_map.json")
TRACKS_MAP_NEW_PATH = os.path.join(
    os.path.dirname(__file__), "maps/tracks_map_new.json"
)

if __name__ == "__main__":
    map_json = load_map(TRACKS_MAP_PATH)

    known_track_names, known_track_hashes = get_known_track_names(map_json)

    print(f"{len(found_track_names)} found track names:")
    print(*sorted(found_track_names), sep="\n")

    potential_track_name_sections = generate_potential_track_name_sections(
        known_track_names + found_track_names + docs_track_names, extras_cap_variants
    )

    sec1_list = potential_track_name_sections
    sep1_list = separators
    sec2_list = potential_track_name_sections
    sep2_list = separators
    sec3_list = potential_track_name_sections
    sep3_list = ["_"]
    sec4_list = [""]
    sep4_list = [""]
    sec5_list = [""]

    search_for_known_hashes(
        sep1_list,
        sec1_list,
        sep2_list,
        sec2_list,
        sep3_list,
        sec3_list,
        sep4_list,
        sec4_list,
        sec5_list,
        known_track_names,
        known_track_hashes,
        TRACKS_MAP_NEW_PATH,
    )
