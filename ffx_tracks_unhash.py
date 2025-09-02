import itertools
from ffx_bones_unhash import BONES_MAP_NEW_PATH
from lists.lists import (
    separators,
    docs_track_names,
    extras,
    numbers,
    numbers_with_leading_zero,
    extras_docs,
    extra_body_parts,
    extra_directions,
    extra_poses,
    extras_blender,
)
from utils.diff_utils import get_extra_sections
from utils.string_utils import (
    generate_potential_track_name_sections,
    generate_ordered_potential_track_name_sections,
    get_capitalisation_variants,
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

    potential_track_name_sections = generate_potential_track_name_sections(
        known_track_names, []
    )

    # sec1_list = potential_track_name_sections
    sep1_list = separators
    # sec2_list = potential_track_name_sections
    sep2_list = separators
    # sec3_list = potential_track_name_sections
    sep3_list = separators
    # sec4_list = ["", "bs", "output"]
    sep4_list = separators
    sep5_list = separators
    # sec5_list = [""]

    sec1_list, sec2_list, sec3_list, sec4_list, sec5_list, sec6_list = (
        generate_ordered_potential_track_name_sections(known_track_names)
    )

    sec1_list = sec1_list + ["Pucker"]
    sec2_list = sec2_list + ["Pucker"]
    sec3_list = sec3_list + ["Pucker"]

    # sec1_list += bone_sections
    # sec2_list += bone_sections
    # sec3_list += sec2_list
    # sec3_list = list(set(sec3_list))
    # sec4_list += sec3_list
    # sec4_list = list(set(sec4_list))
    # sec5_list += sec4_list
    # sec5_list = list(set(sec5_list))
    # sec1_list = potential_track_name_sections
    # sec2_list = potential_track_name_sections
    # sec3_list = potential_track_name_sections
    # sec4_list = sec4_list + numbers + numbers_with_leading_zero
    # sec5_list = sec5_list + numbers + numbers_with_leading_zero
    # sec3_list = list(set(sec3_list + potential_track_name_sections))
    # sec4_list = list(set(sec4_list + tail_list_no_caps))
    # sec5_list = list(
    #     set(tail_list_no_caps + [section + "_bs" for section in tail_list_no_caps])
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
        TRACKS_MAP_NEW_PATH,
    )
