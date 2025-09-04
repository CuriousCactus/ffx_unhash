import re

from ffx_bones_unhash import BONES_MAP_NEW_PATH
from ffx_tracks_unhash import TRACKS_MAP_NEW_PATH
from utils.file_utils import load_map
from utils.string_utils import (
    generate_ordered_potential_track_name_sections,
    get_known_track_names,
)

if __name__ == "__main__":
    tracks_map_json = load_map(TRACKS_MAP_NEW_PATH)
    bones_map_json = load_map(BONES_MAP_NEW_PATH)

    log_file_name = "sections_analysis.log"

    known_bone_names, known_bone_hashes = get_known_track_names(
        bones_map_json,
        log_file_name,
    )

    known_track_names, known_track_hashes = get_known_track_names(
        tracks_map_json,
        log_file_name,
    )

    sec1_list, sec2_list, sec3_list, sec4_list, sec5_list, sec6_list = (
        generate_ordered_potential_track_name_sections(known_bone_names)
    )

    for index, sec_list in enumerate(
        [sec1_list, sec2_list, sec3_list, sec4_list, sec5_list, sec6_list]
    ):
        print("--------------------------------")
        print(f"sec{index + 1}_list")
        print(f"All sections: {sorted(sec_list)}")
        print(
            f"Sections with at least one capital letter: {sorted([x for x in sec_list if re.search('[A-Z]', x)])}"
        )
        print(
            f"Sections with all capital letters: {sorted([x for x in sec_list if re.match('^[A-Z]+$', x)])}"
        )
        print(
            f"Sections with at least one number: {sorted([x for x in sec_list if re.search('[0-9]', x)])}"
        )
        print(
            f"Sections with all numbers: {sorted([x for x in sec_list if re.match('^[0-9]+$', x)])}"
        )
