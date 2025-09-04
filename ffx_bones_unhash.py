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
    generate_ordered_potential_track_name_sections,
    generate_potential_track_name_sections,
    get_capitalisation_variants,
    get_known_track_names,
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

    sep1_list = ["", "_", " "]
    sep2_list = ["", "_", " "]
    sep3_list = ["", "_", " "]
    sep4_list = ["", "_", " "]
    sep5_list = ["", "_", " "]

    sec1_list, sec2_list, sec3_list, sec4_list, sec5_list, sec6_list = (
        generate_ordered_potential_track_name_sections(
            known_bone_names + known_track_names
        )
    )

    # sec6_list = sec5_list
    # sec5_list = sec4_list
    sec1_list = list(
        map(
            lambda y: y.title(),
            #     # extra_body_parts,
            filter(
                # lambda x: x,
                lambda x: len(x) > 2,
                potential_track_name_sections,
                # + extra_body_parts
                # + extra_directions
                # + extra_poses,
                # get_capitalisation_variants(potential_track_name_sections),
                # sec1_list
                # + extra_directions
                # + extra_body_parts,
                # + extra_poses,
                # + extras_blender,
            ),
        )
    )
    # )
    sec2_list = (
        list(
            map(
                lambda y: y.title(),
                # sec2_list,
                filter(
                    lambda x: x,
                    #   re.search("[A-Z]", x) and len(x) > 2,
                    potential_track_name_sections
                    + extra_body_parts
                    + extra_directions
                    + extra_poses,
                    # sec1_list
                    # + extra_directions
                    # + extra_body_parts,
                    # + extra_poses,
                    # + extras_blender,
                    # ),
                ),
            )
        )
        # get_capitalisation_variants(potential_track_name_sections)
        + numbers_with_leading_zero
        + ["", "s", "L", "M", "R", "5", "05", "1"]
    )
    # list(
    #     filter(
    #         lambda x: re.match("^[a-z]+$", x),
    #         # potential_track_name_sections,
    #         sec2_list + extra_directions + extra_body_parts + extra_poses,
    #         # + extras_blender,
    #     )
    # ) + ["1", "01", "001"]
    # sec3_list = sec3_list + extra_body_parts
    sec3_list = list(filter(lambda x: re.search("[A-Z]", x), sec3_list)) + [
        "",
        "s",
        "L",
        "M",
        "R",
        "5",
        "05",
        "1",
        "BS",
    ]
    #     list(map(lambda y: get_capitalisation_variants(y), sec3_list))
    #     # + numbers_with_leading_zero
    #     + ["", "s", "L", "M", "R", "5", "05", "1"]
    # )
    # sec4_list = (
    #     list(map(lambda y: y.title(), sec3_list)) + numbers_with_leading_zero + ["s"]
    # )
    sec4_list = sec3_list + ["BS", "Driver"]
    sec5_list = [""] + ["BS", "Driver"]
    sec6_list = [""] + ["BS", "Driver"]

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
