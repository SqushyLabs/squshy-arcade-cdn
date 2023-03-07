import re
import argparse
from pathlib import Path


def format_data_json(project, version, json_file):
    print(f"Updating {json_file} for {project} @ {version}")
    with open(json_file, 'r') as file:
        data = file.read()

    if "squshy-arcade-cdn" in data:
        return

    sub_folders = ["images", "media", "fonts"]
    for folder in sub_folders:
        data = re.sub(fr'"{folder}/(.*?)"', fr'"https://cdn.jsdelivr.net/gh/SqushyLabs/squshy-arcade-cdn@{version}/{project}/{folder}/\1"', data)

    with open(json_file, "w") as text_file:
        text_file.write(data)


def format_runtimes(project, version, runtime_file):
    print(f"Updating {runtime_file} for {project} @ {version}")
    with open(runtime_file, 'r') as file:
        data = file.read()

    if "squshy.arcade.getC3Data" in data:
        return

    data = data.replace('"data.json"', "squshy.arcade.getC3Data()")

    with open(runtime_file, "w") as text_file:
        text_file.write(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--version')
    args = parser.parse_args()
    data_jsons = [x for x in Path("./").resolve().rglob("*data.json")]
    for data_file in data_jsons:
        format_data_json(data_file.parent.stem, args.version, data_file)

    runtimes = [x for x in Path("./").resolve().rglob("*c3runtime.js")]
    for runtime in runtimes:
        format_runtimes(runtime.parent.stem, args.version, runtime)
