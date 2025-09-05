import re
import time
import itertools
from utils.file_utils import write_log


def print_list(list_to_print, list_name, log_file_name="log.log"):
    header = f"{list_name} (length {len(list_to_print)}):"
    print(header)
    write_log(f"logs\{log_file_name}", header)
    print(sorted(list_to_print))
    write_log(f"logs\{log_file_name}", str(sorted(list_to_print)))


def split_on_separator(known_track_name):
    return re.split(r"[ _-]+", known_track_name)


def split_on_camelcase(known_track_name):
    sections = re.findall(r"[A-Z]?[a-z0-9]+|[A-Z]+(?=[A-Z]|$)", known_track_name)
    if len(sections) <= 1:
        return [known_track_name]
    else:
        return sections


def split(known_track_name):
    if len(split_on_camelcase(known_track_name)) == 1:
        return split_on_separator(known_track_name)
    else:
        return split_on_camelcase(known_track_name)


def get_capitalisation_variants_single(known_track_name):
    lower = known_track_name.lower()
    upper = known_track_name.upper()
    title = known_track_name.title()

    return [
        lower,
        # upper,
        title,
    ]


def get_capitalisation_variants(list_to_cap):
    return list(
        itertools.chain.from_iterable(
            get_capitalisation_variants_single(extra) for extra in list_to_cap
        )
    )


def get_lowercase(list_to_lower):
    return [item.lower() for item in list_to_lower]


def get_known_track_names(map_json, log_file_name):
    known_track_names = []
    known_track_hashes = []
    for key, value in map_json.items():
        known_track_names.extend(value)
        known_track_hashes.append(int(key))

    print_list(known_track_names, "Known track names", log_file_name)

    return known_track_names, known_track_hashes


def generate_potential_track_name_sections(
    known_track_names,
    extras,
    get_cap_variants=False,
    get_extras_cap_variants=False,
    log_file_name="",
):
    potential_track_name_sections = [""]

    for known_track_name in known_track_names:
        sections = split(known_track_name)

        if get_cap_variants:
            potential_track_name_sections.extend(get_capitalisation_variants(sections))
        else:
            potential_track_name_sections.extend(sections)

        if get_extras_cap_variants:
            potential_track_name_sections.extend(get_capitalisation_variants(extras))
        else:
            potential_track_name_sections.extend(extras)

    potential_track_name_sections = list(set(potential_track_name_sections))

    print_list(potential_track_name_sections, "Potential sections", log_file_name)

    return potential_track_name_sections


def generate_ordered_potential_track_name_sections(known_track_names):
    sec1_list = []
    sec2_list = [""]
    sec3_list = [""]
    sec4_list = [""]
    sec5_list = [""]
    sec6_list = [""]

    for known_track_name in known_track_names:
        sections = split(known_track_name)
        if len(sections) > 0:
            sec1_list.append(sections[0])
        if len(sections) > 1:
            sec2_list.append(sections[1])
        if len(sections) > 2:
            sec3_list.append(sections[2])
        if len(sections) > 3:
            sec4_list.append(sections[3])
        if len(sections) > 4:
            sec5_list.append(sections[4])
        if len(sections) > 5:
            sec6_list.append(sections[5])

    return (
        list(set(sec1_list)),
        list(set(sec2_list)),
        list(set(sec3_list)),
        list(set(sec4_list)),
        list(set(sec5_list)),
        list(set(sec6_list)),
    )


def generate_potential_track_names(
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
):
    potential_track_names = (
        f"{sec1}{sep1}{sec2}{sep2}{sec3}{sep3}{sec4}{sep4}{sec5}{sep5}{sec6}"
        for sec1, sep1, sec2, sep2, sec3, sep3, sec4, sep4, sec5, sep5, sec6, in itertools.product(
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
        )
    )

    return potential_track_names
