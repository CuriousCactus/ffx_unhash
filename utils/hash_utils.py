from murmurhash import mrmr
import time
from utils.file_utils import write_track_name
from utils.string_utils import generate_potential_track_names, print_list
from multiprocessing import Pool, cpu_count
from functools import partial

SEED = 0x4EB23


def check_hash(known_track_hashes, track_name):
    generated_track_hash = (
        mrmr.hash64_py(track_name.encode(), seed=SEED) & 0xFFFFFFFFFFFFFFFF
    )

    if generated_track_hash in known_track_hashes:
        return generated_track_hash, track_name
    else:
        return None, None


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
    output_file_name,
):
    start = time.time()

    print_list(sec1_list, "sec1_list")
    print_list(sep1_list, "sep1_list")
    print_list(sec2_list, "sec2_list")
    print_list(sep2_list, "sep2_list")
    print_list(sec3_list, "sec3_list")
    print_list(sep3_list, "sep3_list")
    print_list(sec4_list, "sec4_list")
    print_list(sep4_list, "sep4_list")
    print_list(sec5_list, "sec5_list")

    print("CPU count:", cpu_count())
    pool = Pool(cpu_count())

    re_found_hits = []
    new_hits = []

    total_checkpoints = len(sec1_list)
    checkpoint_index = 0

    while checkpoint_index < total_checkpoints:
        print("----------------------------------------------------")
        print(f"Checkpoint number: {checkpoint_index + 1}/{total_checkpoints}")

        hash_hits_iterator = map(
            partial(check_hash, known_track_hashes),
            generate_potential_track_names(
                sec1_list[checkpoint_index : checkpoint_index + 1],
                sep1_list,
                sec2_list,
                sep2_list,
                sec3_list,
                sep3_list,
                sec4_list,
                sep4_list,
                sec5_list,
            ),
        )

        hash_hits = [x for x in hash_hits_iterator if x[0] is not None]

        for hash_hit, potential_track_name in hash_hits:
            if hash_hit is None:
                continue

            elif potential_track_name in known_track_names:
                print(f"Known hit: {potential_track_name} -> {hash_hit}")
                re_found_hits.append(potential_track_name)

            elif hash_hit is not None:
                print(f"New hit: {potential_track_name} -> {hash_hit}")
                new_hits.append(potential_track_name)
                write_track_name(potential_track_name, hash_hit, output_file_name)

        checkpoint_index += 1

    end = time.time()

    re_found_hits = list(set(re_found_hits))
    new_hits = list(set(new_hits))

    print(f"Time taken: {(end - start)} seconds")

    print_list(re_found_hits, "Known hits")

    if len(re_found_hits) < len(known_track_names):
        print(
            f"Warning: Only re-found {len(re_found_hits)} of {len(known_track_names)} known track names!"
        )
        print_list(sorted(set(known_track_names) - set(re_found_hits)), "Missing")

    print_list(new_hits, "New hits")
