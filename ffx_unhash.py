import itertools
import json
import os
import re
import string
from murmurhash import mrmr

SEED = 0x4EB23
LENGTH = 3
# MAP_PATH = os.path.join(os.path.dirname(__file__), "map.json")
# NEW_MAP_PATH = os.path.join(os.path.dirname(__file__), "new_map.json")
MAP_PATH = os.path.join(os.path.dirname(__file__), "bones_map.json")
NEW_MAP_PATH = os.path.join(os.path.dirname(__file__), "new_bones_map.json")

found_track_names = [
    "Head_Roll_Pos",
    "Head_Pitch_Pos",
    "Head_Yaw_Pos",
    "Rest Pose",
    "lips_funnel",
]

docs_track_names = [
    "PBM",
    "ShCh",
    "Rest Pose",
    "BrowAngry",
    "Head_Pitch_Pos",
    "Head_Yaw_Pos",
    "Head_Roll_Pos",
    "LeftEye_Pitch_Pos",
    "LeftEye_Yaw_Pos",
    "RightEye_Pitch_Pos",
    "RightEye_Yaw_Pos",
    "Head_Pitch_Neg",
    "Head_Yaw_Neg",
    "Head_Roll_Neg",
    "LeftEye_Pitch_Neg",
    "LeftEye_Yaw_Neg",
    "RightEye_Pitch_Neg",
    "RightEye_Yaw_Neg",
    "Look_Up_Lids",
    "Look_Down_Lids",
    "Eyes_Yaw_Neg",
    "Eyes_Yaw_Pos",
    "Eyes_Pitch_Pos",
    "Eyes_Pitch_Neg",
    "Mouth_Sad",
    "Mouth_Anger",
    "Mouth_Happy",
    "Mouth_Snarl",
    "Mouth_Pain",
    "Mouth_Pout",
    "Brows_Sad",
    "Brows_Anger",
    "Brows_Happy",
    "Brows_Pain",
    "CDGKNRSTh",
    "CDGKNRS",
    "CDGKNS",
    "CDGKN",
]

extra_body_parts = [
    "neck",
    "brow",
    "shoulder",
    "eye",
    "eyes",
    "nose",
    "forehead",
    "tongue",
    "palate",
    "jaw",
    "philtrum",
    "larynx",
    "teeth",
    "chin",
    "lid",
    "bone",
]

extra_directions = [
    "in",
    "out",
    "up",
    "down",
    "left",
    "right",
    "high",
    "forward",
    "fw",
    "backward",
    "back",
    "bk",
]

extra_poses = [
    "Frown",
    "Smile",
    "Surprise",
    "Neutral",
    "wrinkle",
    "pout",
    "smirk",
]

ipa = [
    "p",
    "b",
    "t",
    "d",
    "k",
    "g",
    "m",
    "n",
    "ŋ",
    "tʃ",
    "ʃ",
    "dʒ",
    "ʒ",
    "f",
    "v",
    "θ",
    "ð",
    "s",
    "z",
    "ʃ",
    "ʒ",
    "h",
    "w",
    "j",
    "r",
    "l",
    "i",
    "ɪ",
    "e",
    "ɛ",
    "æ",
    "ʌ",
    "ə",
    "u",
    "ʊ",
    "oʊ",
    "ɔ",
    "ɑ",
    "aɪ",
    "ɪ",
    "aʊ",
    "a",
    "ʊ",
    "ɔɪ",
    "ɔ",
    "ɪ",
    "x",
    "ʔ",
]


def split_on_separator(known_track_name):
    return re.split(r"[ _-]+", known_track_name)


def split_on_camelcase(known_track_name):
    sections = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)", known_track_name)
    if len(sections) <= 1:
        return [known_track_name]
    else:
        return sections


def split(known_track_name):
    if len(split_on_camelcase(known_track_name)) == 1:
        return split_on_separator(known_track_name)
    else:
        return split_on_camelcase(known_track_name)


def get_capitalisation_variants(known_track_name):
    lower = known_track_name.lower()
    upper = known_track_name.upper()
    title = known_track_name.title()
    return [lower, upper, title]


def write_track_name(track_name, generated_track_hash):
    with open(NEW_MAP_PATH, "r", encoding="utf-8") as f:
        map_json = json.load(f)

    map_json[str(generated_track_hash)] = [track_name]

    with open(NEW_MAP_PATH, "w", encoding="utf-8") as f:
        json.dump(map_json, f, ensure_ascii=False, indent=4)


def get_known_track_names(map_json):
    known_track_names = []
    known_track_hashes = []
    for key, value in map_json.items():
        known_track_names.extend(value)
        known_track_hashes.append(int(key))

    return known_track_names, known_track_hashes


def generate_potential_track_names(known_track_names):
    extras = (
        ["", "/"]
        + extra_directions
        + extra_body_parts
        + extra_poses
        + [str(i) for i in range(10)]
        + [f"0{i}" for i in range(10)]
        + list(string.ascii_lowercase)
        + ipa
    )

    potential_track_name_sections = []
    for extra in extras:
        potential_track_name_sections.extend(get_capitalisation_variants(extra))

    for known_track_name in known_track_names:
        sections = split(known_track_name)
        for section in sections:
            if LENGTH >= 3:
                capitalised_variants = get_capitalisation_variants(section)
            else:
                capitalised_variants = [section]
            potential_track_name_sections.extend(capitalised_variants)

    potential_track_name_sections = list(set(potential_track_name_sections))
    print(
        f"{len(potential_track_name_sections)} potential sections:",
        sorted(potential_track_name_sections),
    )

    separators = ["", " ", "_", "-"]
    print(f"{len(separators)} separators:", separators)

    if LENGTH == 4:
        potential_track_names = (
            f"{sec1}{sep1}{sec2}{sep2}{sec3}{sep3}{sec4}"
            for sec1, sep1, sec2, sep2, sec3, sep3, sec4 in itertools.product(
                potential_track_name_sections,
                separators,
                potential_track_name_sections,
                separators,
                potential_track_name_sections,
                separators,
                potential_track_name_sections,
            )
        )

    elif LENGTH == 3:
        potential_track_names = (
            f"{sec1}{sep1}{sec2}{sep2}{sec3}"
            for sec1, sep1, sec2, sep2, sec3 in itertools.product(
                potential_track_name_sections,
                separators,
                potential_track_name_sections,
                separators,
                potential_track_name_sections,
            )
        )

    elif LENGTH == 2:
        potential_track_names = (
            f"{sec1}{sep1}{sec2}"
            for sec1, sep1, sec2 in itertools.product(
                potential_track_name_sections,
                separators,
                potential_track_name_sections,
            )
        )

    return potential_track_names


def check_hash(track_name, known_track_names, known_track_hashes, map_json):
    generated_track_hash = (
        mrmr.hash64_py(track_name.encode(), seed=SEED) & 0xFFFFFFFFFFFFFFFF
    )

    if (
        generated_track_hash in known_track_hashes
        and track_name not in known_track_names + found_track_names
    ):
        write_track_name(track_name, generated_track_hash)
        print(f"New hit: {track_name} -> {generated_track_hash}")
    elif track_name in known_track_names:
        write_track_name(track_name, generated_track_hash)
        print(f"Known hit: {track_name} -> {generated_track_hash}")


if __name__ == "__main__":
    with open(MAP_PATH, "r", encoding="utf-8") as f:
        map_json = json.load(f)

    known_track_names, known_track_hashes = get_known_track_names(map_json)
    print(f"{len(known_track_names)} known track names: {sorted(known_track_names)}")

    print(f"{len(found_track_names)} found track names: {found_track_names}")

    potential_track_names = generate_potential_track_names(
        known_track_names + found_track_names + docs_track_names
    )

    for potential_track_name in potential_track_names:
        check_hash(
            potential_track_name,
            known_track_names,
            known_track_hashes,
            map_json,
        )
