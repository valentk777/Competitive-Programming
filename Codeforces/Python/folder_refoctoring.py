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
            return []

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


def _get_all_problems(contest_id: int) -> List[Problem]:
    all_problems = requests.get('https://codeforces.com/api/problemset.problems')
    time.sleep(1)
    all_problems = all_problems.json()["result"]["problems"]
    all_problems = filter(lambda x: x["contestId"] == contest_id, all_problems)
    all_problems = list(map(lambda x: Problem(**x), all_problems))

    return all_problems


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

    return file_paths


def rename_folders(current_path, paths):
    for group in paths:
        folder_path = group[0]
        files = group[1]

        with open(folder_path / files[0], 'r') as f:
            file_data = f.read()

        summary_section = _get_summary_section(file_data)

        if "https://codeforces.com/gym/" in summary_section:
            print("SKIP: ", summary_section)
            continue

        contest_number = _get_contest_number(summary_section)
        contest = _get_all_contests(int(contest_number))[0]

        new_folder_name = contest.name

        rename(group[0], current_path / new_folder_name)


def _get_contest_number(summary_section):
    contest_number = re.findall(r'contest/\d+/problem', summary_section)[0]
    contest_number = re.findall(r'\d+', contest_number)[0]
    return contest_number


def _get_summary_section(data):
    return data.split("# ---------------------------------------------------------------------------------------")[1]


def update_files_summary(paths):
    for group in paths:
        folder_path = group[0]
        files = group[1]

        print(folder_path)

        with open(group[0] / files[0], 'r') as f:
            file_data = f.read()

        summary_section = _get_summary_section(file_data)

        if "https://codeforces.com/gym/" in summary_section:
            print("SKIP: ", summary_section)
            continue

        contest_number = _get_contest_number(summary_section)
        contest = _get_all_contests(int(contest_number))[0]
        problems = _get_all_problems(int(contest_number))

        for file in files:
            with open(group[0] / file, 'r') as f:
                file_data = f.read()

            summary_section = _get_summary_section(file_data)

            problem = list(filter(lambda x: str(x.number) in file, problems))

            if len(problem) == 0:
                print("ERROR!!!!", file)
                continue

            problem = problem[0]

            tags = []

            for division in contest.divisions:
                tags.append(f"tag-div-{division}")

            tags.append(f"tag-difficulty-{problem.rating}")

            temp = summary_section.split("\n")

            if len(temp) != 6:
                temp.append("")

            temp[2] = f"# Title  : {problem.name}"

            new_3 = f"# Tags   : tag-codeforces, tag-problem-{str(problem.number[0])}, {str.join(', ', tags)}"

            if "tag-not-pass" in temp[3]:
                new_3 = new_3 + ", tag-not-pass"

            temp[3] = new_3
            temp[4] = f"# Notes  : {str.join(', ', problem.tags)}"
            new_summary_section = str.join("\n", temp)

            file_data = file_data.replace(summary_section, new_summary_section)

            with open(group[0] / file, 'w') as f:
                f.write(file_data)


if __name__ == "__main__":
    for repo in ["_Regular Rounds"]:
    # for repo in ["_Special Rounds"]:
        # for repo in ["_Global Rounds", "_Educational Rounds", "_Regular Rounds", "_Special Rounds"]:
        file_paths = get_all_files_in_folder(CURRENT_PATH / repo)

        # rename_folders(CURRENT_PATH / repo, file_paths)
        update_files_summary(file_paths)
