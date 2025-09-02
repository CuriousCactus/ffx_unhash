from utils.string_utils import generate_potential_track_name_sections
from utils.file_utils import load_map, get_known_track_names
from utils.hash_utils import check_hash
from ffx_tracks_unhash import TRACKS_MAP_NEW_PATH
from ffx_bones_unhash import BONES_MAP_NEW_PATH

if __name__ == "__main__":
    map_json = load_map(TRACKS_MAP_NEW_PATH)

    known_track_names, known_track_hashes = get_known_track_names(map_json)

    print([name for name in known_track_names if len(name) > 16])
    f = sorted([name for name in known_track_names if "output" in name])
    print(f)
    h = [x.replace("_output", "") for x in f]
    print(h)
    g = sorted([name for name in known_track_names if name not in h + f])
    print(g)

    name = "cornerTight_output"

    result = check_hash(known_track_hashes, False, name)

    print(f"Result for {name}: {result}")
    if result[0] and name not in known_track_names:
        print("TADA")
    elif name in known_track_names:
        print("Already known")
    else:
        print("Not a hit")
