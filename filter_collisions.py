import os
from ffx_unhash import generate_potential_track_name_sections,get_known_track_names, load_map

COLLISIONS_PATH = os.path.join(os.path.dirname(__file__), "786587188986626702.cols")

def filter_collisions():
    map_json = load_map()
    known_track_names, _ = get_known_track_names(map_json)
    potential_track_name_sections = generate_potential_track_name_sections(known_track_names)
    long_sections = list(filter( lambda x: len(x) > 4, potential_track_name_sections))
    print(f"Long sections: {long_sections}")

    with open(COLLISIONS_PATH, "r", encoding="utf-8") as f:
        for line in f:
            for section in long_sections:
                if section in line:
                    print(f"Hit found: {line}")
                    
if __name__ == "__main__":
    filter_collisions()