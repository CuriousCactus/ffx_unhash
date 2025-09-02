import os
from utils.file_utils import load_map, get_known_track_names
from utils.string_utils import generate_potential_track_name_sections, print_list
from ffx_tracks_unhash import TRACKS_MAP_NEW_PATH
from ffx_bones_unhash import BONES_MAP_NEW_PATH
from lists.lists import extras_cap_variants

COLLISIONS_PATH = os.path.join(
    os.path.dirname(__file__), "collisions\\286965447607146401.cols"
)


def filter_collisions():
    tracks_map_json = load_map(TRACKS_MAP_NEW_PATH)
    known_track_names, _ = get_known_track_names(tracks_map_json)
    bones_map_json = load_map(BONES_MAP_NEW_PATH)
    known_bone_names, _ = get_known_track_names(bones_map_json)

    print_list(known_track_names, "Known track names")
    print_list(known_bone_names, "Known bone names")

    potential_track_name_sections = generate_potential_track_name_sections(
        known_track_names + known_bone_names,
        extras_cap_variants,
        get_cap_variants=True,
    )

    long_sections = list(filter(lambda x: len(x) > 4, potential_track_name_sections))

    print_list(long_sections, "Long sections")

    with open(COLLISIONS_PATH, "r", encoding="utf-8") as f:
        for line in f:
            for section in long_sections:
                if section in line:
                    print(f"Hit found: {line}")
            # if len(line) < 15:
            #     print(f"Short line: {line}")
            # for section in long_sections:
            #     if (
            #         line.startswith(section)
            #         and line.count("_") > 1
            #         and line.count("__") == 0
            #     ):
            #         print(f"Hit found: {line}")

            # for section in long_sections:
            #     if line.count(" ") == 4 or line.count("_") == 4:
            #         print(f"Hit found: {line}")
            # if sum(sub in line for sub in long_sections) >= 2:
            #     hits = [sub for sub in long_sections if sub in line]
            #     if (hits[0] not in hits[1]) and (hits[1] not in hits[0]):
            #         print(f"Hit found: {line}", hits)
            # if line[-4:-1] == "_bs":
            #     print(f"Hit found: {line}")
            # if line[-3:-1] == "_r":
            #     print(f"Hit found: {line}")
            # if line[-3:-1] == "_l":
            #     print(f"Hit found: {line}")
            # if line[-3:-1] == "_m":
            #     print(f"Hit found: {line}")


if __name__ == "__main__":
    filter_collisions()
