from ffx_bones_unhash import BONES_MAP_NEW_PATH
from lists.lists import separators, docs_track_names, extras
from utils.diff_utils import get_extra_sections
from utils.string_utils import (
    generate_potential_track_name_sections,
    generate_ordered_potential_track_name_sections,
)
from utils.file_utils import load_map, get_known_track_names
from utils.hash_utils import search_for_known_hashes
import os

TRACKS_MAP_PATH = os.path.join(os.path.dirname(__file__), "maps/tracks_map.json")
TRACKS_MAP_NEW_PATH = os.path.join(
    os.path.dirname(__file__), "maps/tracks_map_new.json"
)

if __name__ == "__main__":
    tracks_map_json = load_map(TRACKS_MAP_NEW_PATH)
    bones_map_json = load_map(BONES_MAP_NEW_PATH)

    known_track_names, known_track_hashes = get_known_track_names(tracks_map_json)
    known_bone_names, known_bone_hashes = get_known_track_names(bones_map_json)

    # potential_track_name_sections = generate_potential_track_name_sections(
    #     known_track_names + docs_track_names, extras
    # )

    # sec1_list = potential_track_name_sections
    sep1_list = separators
    # sec2_list = potential_track_name_sections
    sep2_list = separators
    # sec3_list = potential_track_name_sections
    sep3_list = separators
    # sec4_list = ["", "bs", "output"]
    sep4_list = separators
    # sec5_list = [""]

    sec1_list, sec2_list, sec3_list, sec4_list, sec5_list = (
        generate_ordered_potential_track_name_sections(known_track_names)
    )

    bone_sections = get_extra_sections(known_track_names, known_bone_names)

    sec1_list += bone_sections
    sec2_list += bone_sections
    sec3_list += ["up"]
    sec4_list += sec3_list

    search_for_known_hashes(
        sec1_list,
        sep1_list,
        sec2_list,
        sep2_list,
        sec3_list,
        sep3_list,
        sec4_list,
        sep4_list,
        sec5_list,
        known_track_names,
        known_track_hashes,
        TRACKS_MAP_NEW_PATH,
    )
