import re
import time
from os import walk, getcwd, rename
from pathlib import Path
from typing import List

import requests

CURRENT_PATH = Path(getcwd())


class Contest:
    def __init__(self, id, name, type, phase, frozen, durationSeconds, startTimeSeconds, relativeTimeSeconds):
        self.id = id
        self.name = name.replace("/", "_")
        self.type = type
        self.phase = phase
        self.divisions = self._fill_divisions()

    def _fill_divisions(self):
        if "Div." not in self.name:
            return "2"

        division_numbers = []

        for division_number in self.name.split("Div.")[1:]:
            division_numbers.append(re.findall(r'\d+', division_number)[0])

        return division_numbers


class Problem:
    def __init__(self, contestId, name, index, type="", points=0, rating=0, tags=[]):
        self.contest_id = contestId
        self.name = name
        self.number = index
        self.rating = rating
        self.tags = tags


def _get_all_contests(contest_id: int) -> List[Contest]:
    all_contests = requests.get('https://codeforces.com/api/contest.list?gym=false')
    time.sleep(1)
    all_contests = all_contests.json()["result"]
    all_contests = filter(lambda x: x["id"] == contest_id, all_contests)
    all_contests = list(map(lambda x: Contest(**x), all_contests))
    return all_contests


def get_all_files_in_folder(base_path: Path):
    file_paths = []

    for (dir_path, _, filenames) in walk(base_path):
        if len(filenames) != 0:
            file_paths.append((Path(dir_path), filenames))
        # file_paths.extend(list(map(lambda x: Path(dir_path) / x, filenames)))

    return file_paths


def rename_folders(current_path, paths):
    for folder in paths:
        print(folder[0])

        file_path = folder[1][0]

        with open(folder[0] / file_path, 'r') as f:
            file_data = f.read()

        summary_section = file_data.split(
            "# ---------------------------------------------------------------------------------------"
        )[1]

        if "https://codeforces.com/gym/" in summary_section:
            print("SKIP: ", summary_section)
            continue

        contest_number = re.findall(r'contest/\d+/problem', summary_section)[0]
        contest_number = re.findall(r'\d+', contest_number)[0]
        contest = _get_all_contests(int(contest_number))[0]
        # "contest/709/problem"
        # _get_all_contests()
        new_folder_name = contest.name

        rename(folder[0], current_path / new_folder_name)

if __name__ == "__main__":
    # for repo in ["_Global Rounds", "_Educational Rounds", "_Regular Rounds", "_Special Rounds"]:
    for repo in ["_Regular Rounds"]:

    # folder_path = get_all_files_in_folder(CURRENT_PATH / "_Global Rounds")
    # folder_path = get_all_files_in_folder(CURRENT_PATH / "_Educational Rounds")
    # folder_path = get_all_files_in_folder(CURRENT_PATH / "_Regular Rounds")
        file_paths = get_all_files_in_folder(CURRENT_PATH / repo)

        rename_folders(CURRENT_PATH / repo, file_paths)
