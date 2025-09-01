from utils.string_utils import generate_potential_track_name_sections
from utils.file_utils import load_map, get_known_track_names
from utils.hash_utils import check_hash
from ffx_tracks_unhash import TRACKS_MAP_NEW_PATH
from ffx_bones_unhash import BONES_MAP_NEW_PATH

if __name__ == "__main__":
    map_json = load_map(TRACKS_MAP_NEW_PATH)

    known_track_names, known_track_hashes = get_known_track_names(map_json)

    result = check_hash(known_track_hashes, "cornerClosed")

    print(f"Result: {result}")
