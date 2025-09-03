import json


def load_map(map_path):
    with open(map_path, "r", encoding="utf-8") as f:
        map_json = json.load(f)
    return map_json


def write_log(log_file_name, message):
    with open(log_file_name, "a+", encoding="utf-8") as f:
        f.write(message + "\n")


def write_track_name(track_name, generated_track_hash, output_file_name):
    map_json = load_map(output_file_name)
    map_json[str(generated_track_hash)] = [track_name]

    with open(output_file_name, "w", encoding="utf-8") as f:
        json.dump(map_json, f, ensure_ascii=False, indent=4)
