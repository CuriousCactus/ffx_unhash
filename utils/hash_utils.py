from murmurhash import mrmr
import time
import sys
from utils.file_utils import write_track_name
from utils.string_utils import generate_potential_track_names, print_list
from multiprocessing import Pool, cpu_count, Process
from functools import partial

SEED = 0x4EB23
TIME_PER_CHECK = 832.7087953090668 / 318440176


def split_list_into_chunks(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n)]


def check_hash(known_track_hashes, only_long, track_name):
    if len(track_name) < 16 and only_long:
        return None, None

    generated_track_hash = (
        mrmr.hash64_py(track_name.encode(), seed=SEED) & 0xFFFFFFFFFFFFFFFF
    )

    if generated_track_hash in known_track_hashes:
        return generated_track_hash, track_name
    else:
        return None, None


def check_hashes(
    known_track_hashes,
    known_track_names,
    only_long,
    track_names,
    output_file_name,
    log_file_name,
):
    re_found_hits = []
    new_hits = []

    for track_name in track_names:
        result = check_hash(known_track_hashes, only_long, track_name)
        hash_hit = result[0]

        if hash_hit is None:
            continue

        elif track_name in known_track_names:
            # print(f"Known hit: {track_name} -> {hash_hit}")
            re_found_hits.append(track_name)

        elif hash_hit is not None:
            # print(f"New hit: {track_name} -> {hash_hit}")
            new_hits.append(track_name)
            write_track_name(track_name, hash_hit, output_file_name)

    # re_found_hits = list(set(re_found_hits))
    # new_hits = list(set(new_hits))

    # print_list(re_found_hits, "Known hits", log_file_name)

    # if len(re_found_hits) < len(known_track_names):
    #     print(
    #         f"Warning: Only re-found {len(re_found_hits)} of {len(known_track_names)} known track names!"
    #     )

    #     print_list(
    #         sorted(set(known_track_names) - set(re_found_hits)),
    #         "Missing hits",
    #         log_file_name,
    #     )

    print_list(new_hits, "New hits", log_file_name)


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
    sep5_list,
    sec6_list,
    known_track_names,
    known_track_hashes,
    output_file_name,
    only_long=False,
    log_file_name="",
):
    start = time.time()

    sec1_list = list(set(sec1_list))
    sec2_list = list(set(sec2_list))
    sec3_list = list(set(sec3_list))
    sec4_list = list(set(sec4_list))
    sec5_list = list(set(sec5_list))
    sec6_list = list(set(sec6_list))

    print_list(sec1_list, "sec1_list", log_file_name)
    print_list(sep1_list, "sep1_list", log_file_name)
    print_list(sec2_list, "sec2_list", log_file_name)
    print_list(sep2_list, "sep2_list", log_file_name)
    print_list(sec3_list, "sec3_list", log_file_name)
    print_list(sep3_list, "sep3_list", log_file_name)
    print_list(sec4_list, "sec4_list", log_file_name)
    print_list(sep4_list, "sep4_list", log_file_name)
    print_list(sec5_list, "sec5_list", log_file_name)
    print_list(sep5_list, "sep5_list", log_file_name)
    print_list(sec6_list, "sec6_list", log_file_name)

    total_combinations = (
        len(sec1_list)
        * len(sep1_list)
        * len(sec2_list)
        * len(sep2_list)
        * len(sec3_list)
        * len(sep3_list)
        * len(sec4_list)
        * len(sep4_list)
        * len(sec5_list)
        * len(sep5_list)
        * len(sec6_list)
    )

    print(f"Total combinations to check: {total_combinations}")
    print(
        f"Estimated time to check all combinations: {total_combinations * TIME_PER_CHECK / 3600:.2f} hours"
    )
    print(f"Started at: {time.ctime()}")

    print("CPU count:", cpu_count())

    worker_count = cpu_count()
    worker_pool = []
    chunks = split_list_into_chunks(sec1_list, worker_count)

    for i in range(worker_count):
        p = Process(
            target=check_hashes,
            args=(
                known_track_hashes,
                known_track_names,
                only_long,
                list(
                    generate_potential_track_names(
                        chunks[i],
                        sep1_list,
                        sec2_list,
                        sep2_list,
                        sec3_list,
                        sep3_list,
                        sec4_list,
                        sep4_list,
                        sec5_list,
                        sep5_list,
                        sec6_list,
                    )
                ),
                output_file_name,
                log_file_name,
            ),
        )
        p.start()
        worker_pool.append(p)

    for p in worker_pool:
        p.join()

    end = time.time()

    print(f"Time taken: {(end - start)} seconds")
