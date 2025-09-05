from utils.string_utils import (
    generate_potential_track_name_sections,
    generate_ordered_potential_track_name_sections,
)
from utils.file_utils import load_map
from utils.hash_utils import check_hash, search_for_known_hashes
from ffx_tracks_unhash import TRACKS_MAP_NEW_PATH
from ffx_bones_unhash import BONES_MAP_NEW_PATH
from lists.lists import lower_case_letters
from utils.string_utils import print_list, get_known_track_names

if __name__ == "__main__":
    tracks_map_json = load_map(TRACKS_MAP_NEW_PATH)
    known_track_names, known_track_hashes = get_known_track_names(
        tracks_map_json, "bs.log"
    )
    bones_map_json = load_map(BONES_MAP_NEW_PATH)
    known_bone_names, known_bone_hashes = get_known_track_names(
        bones_map_json, "bs.log"
    )

    tracks_bs_names = [
        known_name for known_name in known_track_names if known_name.endswith("_bs")
    ]
    print_list(tracks_bs_names, "Known track _bs names", "bs.log")

    bones_bs_driver_names = [
        known_name.replace("_driver", "")
        for known_name in known_bone_names
        if known_name.endswith("_bs_driver")
    ]
    print_list(tracks_bs_names, "Known bone _bs_driver names")

    tracks_diff = list(set(bones_bs_driver_names) - set(tracks_bs_names))
    print_list(tracks_diff, "In bones but not in tracks")

    bones_diff = list(set(tracks_bs_names) - set(bones_bs_driver_names))
    print_list(bones_diff, "In tracks but not in bones")

    for name in tracks_diff:
        result = check_hash(known_track_hashes, False, name)

        print("tracks", name, result)

    for name in bones_diff:
        result = check_hash(known_bone_hashes, False, name + "_driver")

        print("bones", name, result)
