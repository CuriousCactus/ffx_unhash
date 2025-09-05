from ffx_bones_unhash import BONES_MAP_NEW_PATH
from utils.file_utils import load_map
from utils.hash_utils import check_hash
from utils.string_utils import (
    generate_potential_track_name_sections,
    get_known_track_names,
)
from utils.file_utils import load_map, write_track_name
from utils.hash_utils import check_hash
from ffx_bones_unhash import BONES_MAP_NEW_PATH

if __name__ == "__main__":
    map_json = load_map(BONES_MAP_NEW_PATH)

    known_track_names, known_track_hashes = get_known_track_names(
        map_json, "message.log"
    )

    name = "Eye_Orbit_L"

    result = check_hash(known_track_hashes, False, name)

    print(f"Result for {name}: {result}")
    if result[0] and name not in known_track_names:
        print("TADA")
        write_track_name(name, result[0], BONES_MAP_NEW_PATH)
    elif name in known_track_names:
        print("Already known")
    else:
        print("Not a hit")
