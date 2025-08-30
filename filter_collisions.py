import os
from utils.file_utils import load_map, get_known_track_names
from utils.string_utils import generate_potential_track_name_sections
from ffx_tracks_unhash import TRACKS_MAP_PATH
from lists.lists import extras_cap_variants

COLLISIONS_PATH = os.path.join(
    os.path.dirname(__file__), "collisions/11514283125473226644.cols"
)


def filter_collisions():
    map_json = load_map(TRACKS_MAP_PATH)
    known_track_names, _ = get_known_track_names(map_json)
    potential_track_name_sections = generate_potential_track_name_sections(
        known_track_names, extras_cap_variants
    )
    long_sections = list(filter(lambda x: len(x) > 4, potential_track_name_sections))
    print(f"Long sections: {long_sections}")

    with open(COLLISIONS_PATH, "r", encoding="utf-8") as f:
        for line in f:
            for section in long_sections:
                if section in line:
                    print(f"Hit found: {line}")


if __name__ == "__main__":
    filter_collisions()
