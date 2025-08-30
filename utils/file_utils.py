import json
import os


def load_map(map_path):
    with open(map_path, "r", encoding="utf-8") as f:
        map_json = json.load(f)
    return map_json


def write_track_name(track_name, generated_track_hash, output_file_name):
    map_json = load_map(output_file_name)
    map_json[str(generated_track_hash)] = [track_name]

    with open(output_file_name, "w", encoding="utf-8") as f:
        json.dump(map_json, f, ensure_ascii=False, indent=4)


def get_known_track_names(map_json):
    known_track_names = []
    known_track_hashes = []
    for key, value in map_json.items():
        known_track_names.extend(value)
        known_track_hashes.append(int(key))

    print(f"{len(known_track_names)} known track names:")
    print(*sorted(known_track_names), sep="\n")

    return known_track_names, known_track_hashes
