from murmurhash import mrmr
import time
from file_utils import write_track_name
from string_utils import generate_potential_track_names

SEED = 0x4EB23


def check_hash(track_name, known_track_hashes):
    generated_track_hash = (
        mrmr.hash64_py(track_name.encode(), seed=SEED) & 0xFFFFFFFFFFFFFFFF
    )

    if generated_track_hash in known_track_hashes:
        return generated_track_hash
    else:
        return None


def search_for_known_hashes(
    sec1_list,
    sep1_list,
    sec2_list,
    sep2_list,
    sec3_list,
    sep3_list,
    sec4_list,
    sep4_list,
    sec5_list,
    known_track_names,
    known_track_hashes,
):
    potential_track_names = generate_potential_track_names(
        sec1_list,
        sep1_list,
        sec2_list,
        sep2_list,
        sec3_list,
        sep3_list,
        sec4_list,
        sep4_list,
        sec5_list,
    )

    start = time.time()
    re_found_hits = []
    new_hists = []
    for potential_track_name in potential_track_names:
        hash_hit = check_hash(potential_track_name, known_track_hashes)

        if hash_hit in known_track_hashes:
            print(f"Known hit: {potential_track_name} -> {hash_hit}")
            re_found_hits.append(potential_track_name)

        elif hash_hit is not None:
            print(f"New hit: {potential_track_name} -> {hash_hit}")
            new_hists.append(potential_track_name)
            write_track_name(potential_track_name, hash_hit)

    end = time.time()

    print(f"Time taken: {(end - start)/ 3600:.2f} hours")

    print(f"Re-found {len(re_found_hits)} known hits: {re_found_hits}")

    if len(re_found_hits) < len(known_track_names):
        print(
            f"Warning: Only re-found {len(re_found_hits)} of {len(known_track_names)} known track names!"
        )
        print(f"Missing: {sorted(set(known_track_names) - set(re_found_hits))}")

    print(f"Found {len(new_hists)} new hits: {new_hists}")
