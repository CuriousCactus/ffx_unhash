from utils.string_utils import (
    generate_potential_track_name_sections,
    generate_ordered_potential_track_name_sections,
    get_known_track_names,
)
from utils.file_utils import load_map
from utils.hash_utils import check_hash, search_for_known_hashes
from ffx_tracks_unhash import TRACKS_MAP_NEW_PATH
from ffx_bones_unhash import BONES_MAP_NEW_PATH
from lists.lists import lower_case_letters
from utils.string_utils import print_list

import random


def generate_unique_names(existing, count):
    prefixes = [
        "beard",
        "brow",
        "cheek",
        "chin",
        "eye",
        "eyebrow",
        "gullet",
        "jaw",
        "lips",
        "lobe",
        "lower_cheek",
        "lowerlip",
        "nose",
        "piercing",
        "smilelines",
        "sneer",
        "squint",
        "tongue",
        "upperlip",
        "wrinkle",
        "ear",
        "temple",
        "forehead",
        "neck",
        "nostril",
        "septum",
        "tragus",
        "philtrum",
        "jawline",
        "lip",
        "mouth",
        "eyelid",
        "lid",
        "pupil",
        "iris",
        "tear",
        "lash",
        "socket",
        "orbital",
        "nasal",
        "mandible",
        "maxilla",
    ]
    suffixes = [
        "l",
        "r",
        "m",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "edge",
        "base",
        "tip",
        "wing",
        "bridge",
        "under",
        "upper",
        "lower",
        "outer",
        "inner",
        "central",
        "mid",
        "main",
        "driver",
        "bs",
        "output",
        "rollin",
        "rollout",
        "up",
        "dn",
        "raise",
        "lower",
        "squeeze",
        "smile",
        "frown",
        "funnel",
        "narrow",
        "wide",
        "open",
        "close",
        "sneer",
        "squint",
        "pucker",
        "press",
        "curl",
        "spread",
        "twist",
        "shrug",
    ]
    connectors = ["_", ""]
    extra_numbers = [str(i).zfill(2) for i in range(21, 100)]
    suffixes += extra_numbers

    generated = set(existing)
    result = []

    while len(result) < count:
        prefix = random.choice(prefixes)
        connector = random.choice(connectors)
        mid = random.choice(suffixes)
        connector2 = random.choice(connectors)
        end = random.choice(suffixes)
        name = f"{prefix}{connector}{mid}{connector2}{end}"
        # Ensure no overlap with existing and no repeats
        if name not in generated:
            generated.add(name)
            result.append(name)

    return result


if __name__ == "__main__":

    tracks_map_json = load_map(TRACKS_MAP_NEW_PATH)
    bones_map_json = load_map(BONES_MAP_NEW_PATH)

    known_track_names, known_track_hashes = get_known_track_names(
        tracks_map_json, "spec.log"
    )
    known_bone_names, known_bone_hashes = get_known_track_names(
        bones_map_json, "spec.log"
    )

    new_names = generate_unique_names(known_track_names + known_bone_names, 5000)
    print(new_names)

    for name in new_names:
        result = check_hash(known_bone_hashes, False, name + "_driver")
        if result[0]:
            print("bones", name, result)
