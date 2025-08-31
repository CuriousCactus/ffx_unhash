from utils.string_utils import (
    generate_potential_track_name_sections,
    generate_ordered_potential_track_name_sections,
)
from utils.file_utils import load_map, get_known_track_names
from utils.hash_utils import check_hash, search_for_known_hashes
from lists.lists import lower_case_letters
from utils.string_utils import print_list


def get_long_sections(known_track_names):
    track_sections = generate_potential_track_name_sections(known_track_names, [])

    long_track_sections = [
        track_section for track_section in track_sections if len(track_section) > 2
    ]

    print_list(long_track_sections, "Long track sections")

    return long_track_sections


def get_extra_sections(primary_track_names, secondary_track_names):
    primary_sections = get_long_sections(primary_track_names)
    secondary_sections = get_long_sections(secondary_track_names)
    diff = list(set(secondary_sections) - set(primary_sections))

    print_list(diff, "Diff")

    return diff
