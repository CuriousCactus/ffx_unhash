import os
from fnvhash import fnv, fnv1_32, fnv1a_32, fnv0_32, fnv0_64, fnv1_64, fnv1a_64, fnva
from ffx_bones_unhash import BONES_MAP_NEW_PATH
from utils.file_utils import load_map
from utils.hash_utils import check_hash
from utils.string_utils import (
    generate_potential_track_name_sections,
    get_known_track_names,
)
from utils.file_utils import load_map, write_track_name
from utils.hash_utils import check_hash, search_for_known_hashes
from ffx_bones_unhash import BONES_MAP_NEW_PATH
from lists.blender_bones import blender_bones
from lists.blender_error_bones import blender_error_bones
from utils.string_utils import (
    filter_no_numbers,
    generate_ordered_potential_track_name_sections,
    generate_potential_track_name_sections,
    get_capitalisation_variants,
    get_known_track_names,
    map_to_title,
)
import datetime

WEM_MAP_NEW_PATH = os.path.join(os.path.dirname(__file__), "maps/wem_map.json")
SOUND_EVENTS_MAP_NEW_PATH = os.path.join(
    os.path.dirname(__file__),
    "maps/sound_events_map.json",
)

if __name__ == "__main__":
    log_file_name = (
        f"{str(datetime.datetime.now()).replace(' ', '-').replace(':','-')}.log"
    )

    sound_events_map_json = load_map(SOUND_EVENTS_MAP_NEW_PATH)

    known_sound_event_names, known_sound_event_hashes = get_known_track_names(
        sound_events_map_json,
        log_file_name,
    )

    sec1_list, sec2_list, sec3_list, sec4_list, sec5_list, sec6_list = (
        generate_ordered_potential_track_name_sections(known_sound_event_names)
    )

    sep1_list = ["", "_"]
    sep2_list = ["", "_"]
    sep3_list = ["", "_"]
    sep4_list = ["", "_"]
    sep5_list = ["", "_"]

    sec1_list = known_sound_event_names
    sec2_list = [""]
    sec3_list = [""]
    sec4_list = [""]
    sec5_list = [""]
    sec6_list = [""]

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
        known_sound_event_names,
        known_sound_event_hashes,
        SOUND_EVENTS_MAP_NEW_PATH,
        False,
        log_file_name,
        hash_algorithm="fnv",
    )
