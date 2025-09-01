from lists.lists import (
    separators,
    docs_track_names,
    lower_case_letters,
    numbers_with_leading_zero,
    numbers,
    extras_no_cap_variants,
    extra_body_parts,
    extras_blender,
)
from utils.string_utils import (
    generate_potential_track_name_sections,
    generate_ordered_potential_track_name_sections,
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

    # potential_track_name_sections_no_numbers = list(
    #     filter(
    #         lambda x: x not in numbers_with_leading_zero + numbers,
    #         potential_track_name_sections,
    #     )
    # )

    # potential_track_name_sections_short = list(
    #     filter(lambda x: len(x) <= 2, potential_track_name_sections)
    # ) + ["driver"]

    # sec1_list = potential_track_name_sections_no_numbers
    sep1_list = ["", "_"]
    # sec2_list = potential_track_name_sections
    sep2_list = ["", "_"]
    # sec3_list = potential_track_name_sections + [""]
    sep3_list = ["", "_"]
    # sec4_list = (
    #     list(range(4))
    #     + numbers_with_leading_zero
    #     + potential_track_name_sections_short
    #     + [""]
    # )
    sep4_list = ["", "_"]
    # sec5_list = [""]

    sec1_list, sec2_list, sec3_list, sec4_list, sec5_list = (
        generate_ordered_potential_track_name_sections(known_track_names)
    )

    # sec4_list = list(set(sec3_list))
    # sec1_list = list(set(sec1_list + sec2_list + extra_body_parts))
    # sec2_list = sec1_list
    # sec3_list = sec1_list

    # sec5_list = list(
    #     set(sec4_list + sec5_list + [sec + "_driver" for sec in sec4_list])
    # )
    # sec4_list = list(set(sec4_list))
    # sec1_list = list(set(potential_track_name_sections))
    # sec2_list = list(set(potential_track_name_sections))
    # sec3_list = list(set(sec3_list))
    sec1_list = ["piercing"]
    sec2_list = ["helix", "lobe", "bridge", "nostril"]

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
        BONES_MAP_NEW_PATH,
    )
