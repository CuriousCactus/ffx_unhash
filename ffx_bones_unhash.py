import datetime
import os
import re

from lists.lists import (
    extra_body_parts,
    extra_directions,
    extra_poses,
    numbers_with_leading_zero,
)
from utils.file_utils import load_map
from utils.hash_utils import search_for_known_hashes
from utils.string_utils import (
    filter_no_numbers,
    generate_ordered_potential_track_name_sections,
    generate_potential_track_name_sections,
    get_capitalisation_variants,
    get_known_track_names,
    map_to_title,
)

BONES_MAP_NEW_PATH = os.path.join(os.path.dirname(__file__), "maps/bones_map_new.json")
TRACKS_MAP_NEW_PATH = os.path.join(
    os.path.dirname(__file__), "maps/tracks_map_new.json"
)

if __name__ == "__main__":
    tracks_map_json = load_map(TRACKS_MAP_NEW_PATH)
    bones_map_json = load_map(BONES_MAP_NEW_PATH)

    log_file_name = (
        f"{str(datetime.datetime.now()).replace(' ', '-').replace(':','-')}.log"
    )

    known_bone_names, known_bone_hashes = get_known_track_names(
        bones_map_json,
        log_file_name,
    )

    known_track_names, known_track_hashes = get_known_track_names(
        tracks_map_json,
        log_file_name,
    )

    potential_track_name_sections = generate_potential_track_name_sections(
        known_bone_names + known_track_names, [], False, False, log_file_name
    )

    # sep1_list = ["", "_", " "]
    # sep2_list = ["", "_", " "]
    # sep3_list = ["", "_", " "]
    # sep4_list = ["", "_", " "]
    # sep5_list = ["", "_", " "]
    sep1_list = ["", "_"]
    sep2_list = ["", "_"]
    sep3_list = ["", "_"]
    sep4_list = ["", "_"]
    sep5_list = ["", "_"]

    sec1_list, sec2_list, sec3_list, sec4_list, sec5_list, sec6_list = (
        generate_ordered_potential_track_name_sections(known_bone_names)
    )

    # sec1_list = map_to_title(
    #     filter_no_numbers(
    #         sec1_list
    #         + extra_body_parts
    #         + extra_poses
    #         + extra_directions
    #         + potential_track_name_sections
    #     )
    # )
    # sec2_list = map_to_title(
    #     sec2_list + extra_body_parts + extra_directions + potential_track_name_sections
    # ) + ["", "1"]
    # sec3_list = map_to_title(sec3_list) + [""]
    # sec4_list = map_to_title(sec4_list) + [""]
    # sec5_list = map_to_title(sec5_list) + [""]
    # sec6_list = map_to_title(sec6_list) + [""]
    sec1_list = ["jugal", "Jugal"]
    sec2_list = ["l", "r", "L", "R"]
    sec3_list = numbers_with_leading_zero
    # sec3_list = ["FR", "FL", "BR", "BL"]

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
        sep5_list,
        sec6_list,
        known_bone_names,
        known_bone_hashes,
        BONES_MAP_NEW_PATH,
        False,
        log_file_name,
    )
