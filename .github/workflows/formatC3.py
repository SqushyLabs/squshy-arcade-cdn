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


def format_file(project, version, runtime_file, search_text, replace_text):
    print(f"Updating {runtime_file} for {project} @ {version}")
    with open(runtime_file, 'r') as file:
        data = file.read()

    if replace_text in data:
        return

    data = data.replace(search_text, replace_text)

    with open(runtime_file, "w") as text_file:
        text_file.write(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--version')
    args = parser.parse_args()
    data_jsons = [x for x in Path("./").resolve().rglob("*data.json")]
    for data_file in data_jsons:
        format_data_json(data_file.parent.stem, args.version, data_file)

    files_to_format = [
        'c3runtime.js', 'main.js', 'register-sw.js'
    ]

    search_replace = {
        '"data.json"': "squshy.arcade.getC3File('data.json')",
        '"scripts/c3runtime.js"': "squshy.arcade.getC3File('scripts/c3runtime.js')",
        'workerMainUrl:"workermain.js"': "workerMainUrl:squshy.arcade.getC3File('workermain.js')",
        'this._GetWorkerScriptFolder()': "squshy.arcade.getC3File('scripts/')",
        'console.info("Made with Construct, the game and app creator :: https://www.construct.net")': "squshy.arcade.gameLoaded()"
    }

    for file in files_to_format:
        found_files = [x for x in Path("./").resolve().rglob(f"*{file}")]
        for found_file in found_files:
            for search, replace in search_replace.items():
                format_file(
                    project=found_file.parent.stem,
                    version=args.version,
                    runtime_file=found_file,
                    search_text=search,
                    replace_text=replace
                )
