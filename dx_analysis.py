import os
import re

from ffx_bones_unhash import BONES_MAP_NEW_PATH
from ffx_tracks_unhash import TRACKS_MAP_NEW_PATH
from utils.file_utils import load_map
from utils.string_utils import (
    generate_ordered_potential_track_name_sections,
    get_known_track_names,
    print_list,
)

BONES_MAP_DX_NEW_PATH = os.path.join(
    os.path.dirname(__file__), "maps/tracks_map_b4.json"
)

if __name__ == "__main__":
    bones_map_dx_json = load_map(BONES_MAP_DX_NEW_PATH)

    log_file_name = "dx_analysis.log"

    potential_bone_names, known_bone_hashes = get_known_track_names(
        bones_map_dx_json,
        log_file_name,
    )

    separators = ["_", " "]

    hits = []
    for potential_bone_name in potential_bone_names:
        for i, sep in enumerate(separators):
            if (
                potential_bone_name.count(sep) > 0
                and potential_bone_name.count(sep) < 4
                and potential_bone_name[0] != sep
                and potential_bone_name[-1] != sep
                and not re.match("[A-Z]", potential_bone_name[-1])
                and not re.match("[0-9][a-zA-Z]", potential_bone_name)
                and not re.match("[A-Z][A-Z]", potential_bone_name)
                and not re.match(
                    "[aeiouAEIOU][aeiouAEIOU][aeiouAEIOU]", potential_bone_name
                )
                and potential_bone_name.count(separators[i - 1]) == 0
                and len(re.findall("[0-9]", potential_bone_name)) < 3
                and not potential_bone_name[0].isdigit()
            ):
                hits.append(potential_bone_name)

    print_list(list(set(hits)), "Hits", "dx.log", "\n")
    # print(*list(sorted(list(set(hits)))), sep="\n")
