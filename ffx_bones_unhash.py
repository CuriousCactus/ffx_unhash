from lists.lists import (
    separators,
    docs_track_names,
    lower_case_letters,
    numbers_with_leading_zero,
    numbers,
    extras_no_cap_variants,
    extra_body_parts,
    extras_blender,
    extras,
    extra_directions,
    extra_poses,
    extras_docs,
)
from utils.string_utils import (
    generate_potential_track_name_sections,
    generate_ordered_potential_track_name_sections,
    get_lowercase,
    print_list,
)
from utils.file_utils import load_map, get_known_track_names
from utils.hash_utils import search_for_known_hashes
import os


BONES_MAP_PATH = os.path.join(os.path.dirname(__file__), "maps/bones_map.json")
BONES_MAP_NEW_PATH = os.path.join(os.path.dirname(__file__), "maps/bones_map_new.json")


if __name__ == "__main__":
    map_json = load_map(BONES_MAP_NEW_PATH)

    known_track_names, known_track_hashes = get_known_track_names(map_json)

    potential_track_name_sections = generate_potential_track_name_sections(
        known_track_names,
        [],
    )

    sep1_list = ["", "_"]
    sep2_list = ["", "_"]
    sep3_list = ["", "_"]
    sep4_list = ["", "_"]
    sep5_list = ["", "_"]

    sec1_list, sec2_list, sec3_list, sec4_list, sec5_list, sec6_list = (
        generate_ordered_potential_track_name_sections(known_track_names)
    )

    sec6_list = sec5_list
    sec5_list = sec4_list
    sec1_list = sec1_list + get_lowercase(
        extra_directions + extra_body_parts + extra_poses + extras_blender + extras_docs
    )
    sec2_list = sec2_list + get_lowercase(
        extra_directions + extra_body_parts + extra_poses + extras_blender + extras_docs
    )
    # sec3_list = sec3_list + get_lowercase(
    #     extra_directions + extra_body_parts + extra_poses + extras_blender + extras_docs
    # )

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
        known_track_names,
        known_track_hashes,
        BONES_MAP_NEW_PATH,
    )
