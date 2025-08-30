import json
import os
from lists import found_track_names

MAP_PATH = os.path.join(os.path.dirname(__file__), "map.json")
NEW_MAP_PATH = os.path.join(os.path.dirname(__file__), "new_map.json")
BONES_MAP_PATH = os.path.join(os.path.dirname(__file__), "bones_map.json")
NEW_BONES_MAP_PATH = os.path.join(os.path.dirname(__file__), "new_bones_map.json")


def load_map():
    with open(MAP_PATH, "r", encoding="utf-8") as f:
        map_json = json.load(f)
    return map_json


def load_new_map():
    with open(NEW_MAP_PATH, "r", encoding="utf-8") as f:
        new_map_json = json.load(f)
    return new_map_json


def load_bones_map():
    with open(BONES_MAP_PATH, "r", encoding="utf-8") as f:
        map_json = json.load(f)
    return map_json


def load_new_map():
    with open(NEW_BONES_MAP_PATH, "r", encoding="utf-8") as f:
        new_map_json = json.load(f)
    return new_map_json


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

    print(f"{len(known_track_names)} known track names: {sorted(known_track_names)}")
    print(f"{len(found_track_names)} found track names: {found_track_names}")

    return known_track_names, known_track_hashes
