from utils.string_utils import generate_potential_track_name_sections, print_list
from utils.file_utils import load_map, get_known_track_names
from utils.hash_utils import check_hash
from ffx_tracks_unhash import TRACKS_MAP_NEW_PATH
from ffx_bones_unhash import BONES_MAP_NEW_PATH
import os

FREQUENCIES_PATH = os.path.join(os.path.dirname(__file__), "data/frequencies.json")


def analyse(hash_list):
    result = {}
    for hash in hash_list:
        print(f"Hash: {hash}")
        unknown_frequency = frequencies_json[hash]
        print(f"Frequency {unknown_frequency}")
        matching_frequencies = [
            fhash
            for fhash, frequency in frequencies_json.items()
            if frequency == unknown_frequency
        ]
        matching_names = [
            name_list[0]
            for hash, name_list in map_json.items()
            if len(name_list) and hash in matching_frequencies
        ]
        print_list(sorted(matching_names), "Tracks with the same frequencies")

        result[hash] = matching_names

    return result


if __name__ == "__main__":
    map_json = load_map(TRACKS_MAP_NEW_PATH)
    frequencies_json = load_map(FREQUENCIES_PATH)

    known_track_names, known_track_hashes = get_known_track_names(map_json)

    unknowns = [
        # "5653735459566580575",
        "17054254757116529680",
        "286965447607146401",
    ]

    common_knowns = ["1380675382255544665", "1860960753336841273"]

    outputs = analyse(unknowns)
    # ["5653735459566580575"]  # should end with _output
    # parents = analyse(common_knowns)["1380675382255544665"]
    # missing = list(set(parents) - set([x.replace("_output", "") for x in outputs]))
    # missing_outputs = [m + "_output" for m in missing]
    # print(missing)
    # print(missing_outputs)
    # for m in missing_outputs:
    #     print(check_hash(known_track_hashes, False, m))

    # Should exist but don't
    # ['wide_output', 'rollin_output', 'rollout_output', 'upLipDn_output', 'lowLipUp_output', 'upFunnel_output', 'narrow_output']
    # ['lowerlip_rollout_bs', 'upperlip_rollout_bs']
