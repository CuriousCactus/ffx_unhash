import itertools
import os
import re

from utils.file_utils import write_log

TIME_PER_CHECK = 1150 / 507744000


def print_list(list_to_print, list_name, log_file_name="log.log", separator=None):
    header = f"{list_name} (length {len(list_to_print)}):"
    print(header)
    write_log(os.path.join("logs", log_file_name), header)
    if separator is None:
        print(sorted(list_to_print))
    else:
        print(*sorted(list_to_print), sep=separator)
    write_log(os.path.join("logs", log_file_name), str(sorted(list_to_print)))


def log_combinations(
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
    # upper = known_track_name.upper()
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
    sec1_list: list[str],
    sep1_list: list[str],
    sec2_list: list[str],
    sep2_list: list[str],
    sec3_list: list[str],
    sep3_list: list[str],
    sec4_list: list[str],
    sep4_list: list[str],
    sec5_list: list[str],
    sep5_list: list[str],
    sec6_list: list[str],
):
    print(f"Checking {sec1_list[0]}")

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


def filter_lowercase_only(strings: list[str]) -> list[str]:
    return [s for s in strings if s.islower()]


def filter_contains_lowercase(strings: list[str]) -> list[str]:
    return [s for s in strings if any(c.islower() for c in s)]


def filter_no_lowercase(strings: list[str]) -> list[str]:
    return [s for s in strings if not any(c.islower() for c in s)]


def filter_no_uppercase(strings: list[str]) -> list[str]:
    return [s for s in strings if not any(c.isupper() for c in s)]


def filter_no_numbers(strings: list[str]) -> list[str]:
    return [s for s in strings if not any(c.isdigit() for c in s)]


def map_to_title(strings: list[str]) -> list[str]:
    return [s.title() for s in strings]
