import re
import time
import itertools

TIME_PER_CHECK = 832.7087953090668 / 318440176


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

    return [
        lower,
        # upper,
        title,
    ]


def generate_potential_track_name_sections(known_track_names, extras):
    potential_track_name_sections = []

    for known_track_name in known_track_names:
        sections = split(known_track_name)
        for section in sections:
            capitalised_variants = [section]
            potential_track_name_sections.extend(capitalised_variants)

    potential_track_name_sections.extend(extras)
    potential_track_name_sections = list(set(potential_track_name_sections))

    print(
        f"{len(potential_track_name_sections)} potential sections: {potential_track_name_sections}"
    )

    return potential_track_name_sections


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
):
    potential_track_names = (
        f"{sec1}{sep1}{sec2}{sep2}{sec3}{sep3}{sec4}{sep4}{sec5}"
        for sec1, sep1, sec2, sep2, sec3, sep3, sec4, sep4, sec5 in itertools.product(
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
    )

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
    )

    print(f"Total combinations to check: {total_combinations}")
    print(
        f"Estimated time to check all combinations: {total_combinations * TIME_PER_CHECK / 3600:.2f} hours"
    )
    print(f"Started at: {time.ctime()}")

    return potential_track_names
