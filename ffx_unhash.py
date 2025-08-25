import json
import os
import re
from turtle import title
from murmurhash import mrmr

SEED = 0x4EB23
LONG = True
MAP_PATH = os.path.join(os.path.dirname(__file__), "map.json")


def get_known_track_names():

    with open(MAP_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    known_track_names = []
    known_track_hashes = []
    for key, value in data.items():
        known_track_names.extend(value)
        known_track_hashes.append(int(key))

    return known_track_names, known_track_hashes


def check_hashes(track_names, known_track_names, known_track_hashes):
    generated_track_hashes = []
    new_hits = []
    known_hits = []
    fails = []
    for track_name in track_names:
        generated_track_hash = (
            mrmr.hash64_py(track_name.encode(), seed=SEED) & 0xFFFFFFFFFFFFFFFF
        )

        if (
            generated_track_hash in known_track_hashes
            and track_name not in known_track_names
            and track_name not in new_hits
        ):
            new_hits.append(track_name)
        elif track_name in known_track_names and track_name not in known_hits:
            known_hits.append(track_name)
        else:
            fails.append(track_name)

        generated_track_hashes.append(generated_track_hash)

    print(f"{len(known_hits)} known hits:", known_hits)
    print(f"{len(new_hits)} new hits:", new_hits)
    print(f"{len(fails)} fails")


def split_separator(known_track_name):
    return re.split(r"[ _-]+", known_track_name)


def split_camelcase(known_track_name):
    sections = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)", known_track_name)
    if len(sections) <= 1:
        return [known_track_name]
    else:
        return sections


def split(known_track_name):
    if len(split_camelcase(known_track_name)) == 1:
        return split_separator(known_track_name)
    else:
        return split_camelcase(known_track_name)


def get_capitalisation_variants(known_track_name):
    lower = known_track_name.lower()
    upper = known_track_name.upper()
    title = known_track_name.title()
    return [lower, upper, title]


def generate_potential_track_names(known_track_names):
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
    ]
    extra_directions = [
        "in",
        "out",
        "down",
        "left",
        "right",
        "high",
        "forward",
        "backward",
        "back",
    ]
    extras = [""] + extra_directions + extra_body_parts

    potential_track_name_sections = []
    for extra in extras:
        potential_track_name_sections.extend(get_capitalisation_variants(extra))

    for known_track_name in known_track_names:
        sections = split(known_track_name)
        for section in sections:
            if LONG:
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
    if LONG:
        potential_track_names = [
            f"{sec1}{sep1}{sec2}{sep2}{sec3}{sep3}{sec4}"
            for sec1 in potential_track_name_sections
            for sec2 in potential_track_name_sections
            for sec3 in potential_track_name_sections
            for sec4 in potential_track_name_sections
            for sep1 in separators
            for sep2 in separators
            for sep3 in separators
        ]
    else:
        potential_track_names = [
            f"{sec1}{sep1}{sec2}"
            for sec1 in potential_track_name_sections
            for sec2 in potential_track_name_sections
            for sep1 in separators
        ]

    return potential_track_names


if __name__ == "__main__":
    known_track_names, known_track_hashes = get_known_track_names()
    print(f"{len(known_track_names)} known track names: {sorted(known_track_names)}")

    found_track_names = ["Head_Roll_Pos", "Head_Pitch_Pos", "Head_Yaw_Pos"]
    print(f"{len(found_track_names)} found track names: {found_track_names}")

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
    ]

    potential_track_names = generate_potential_track_names(
        known_track_names + found_track_names + docs_track_names
    )

    check_hashes(
        potential_track_names + docs_track_names,
        known_track_names,
        known_track_hashes,
    )
