from lists import (
    separators,
    found_track_names,
    docs_track_names,
    lower_case_letters,
    number_with_leading_zeros,
    extras,
)
from string_utils import generate_potential_track_name_sections
from file_utils import load_bones_map, get_known_track_names
from hash_utils import search_for_known_hashes


if __name__ == "__main__":
    map_json = load_bones_map()

    known_track_names, known_track_hashes = get_known_track_names(map_json)

    potential_track_name_sections = generate_potential_track_name_sections(
        known_track_names,
        extras,
    )

    sec1_list = potential_track_name_sections
    sep1_list = ["_"]
    sec2_list = potential_track_name_sections
    sep2_list = ["_"]
    sec3_list = potential_track_name_sections + number_with_leading_zeros + [""]
    sep3_list = ["", "_"]
    sec4_list = number_with_leading_zeros + [""]
    sep4_list = [""]
    sec5_list = [""]

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
    )
