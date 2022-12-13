import logging
import re
import shutil
import webbrowser
from os import getcwd, mkdir, path
from pathlib import Path
from typing import List

import requests

logger = logging.getLogger()
logger.setLevel(1)

CURRENT_PATH = Path(getcwd())


class Problem:
    def __init__(self, contestId, name, index, type="", points=0, rating=0, tags=[]):
        self.contest_id = contestId
        self.name = name
        self.number = index
        self.rating = rating
        self.tags = tags


class Contest:
    def __init__(self, id, name, type, phase, frozen, durationSeconds, startTimeSeconds, relativeTimeSeconds):
        self.id = id
        self.name = name.replace("/", "_").replace(":", " ")
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


class RoundData:
    def __init__(self, web_url, contest_id: int = 0, is_started=True):
        self.web_url = web_url
        self.contest_id = self._get_contest_id() if contest_id == 0 else contest_id
        self.is_started = is_started
        self.problems = None

        self._set_problems()

        self.contest = self._get_full_contest()

    def _get_all_problems(self, contest_id: int) -> List[Problem]:
        all_problems = requests.get('https://codeforces.com/api/problemset.problems')
        all_problems = all_problems.json()["result"]["problems"]
        all_problems = filter(lambda x: x["contestId"] == contest_id, all_problems)
        all_problems = list(map(lambda x: Problem(**x), all_problems))

        return all_problems

    def _set_problems(self) -> None:
        if self.problems is not None:
            return self.problems

        if self.is_started:
            all_problems = self._get_all_problems(self.contest_id)
        else:
            all_problems = map(lambda x: chr(x), range(ord("A"), ord("G") + 1))
            all_problems = list(map(lambda idx: Problem(self.contest_id, "", idx), all_problems))

        if "problem" not in self.web_url:
            self.problems = all_problems
            return

        problems_number = self._get_problem_number_from_url()

        selected_problem = list(filter(lambda problem: problem.number == problems_number, all_problems))

        if len(selected_problem) == 0:
            raise Exception("problem was not found")

        self.problems = selected_problem

    def _get_problem_number_from_url(self) -> str:
        problems_number = self.web_url.split("problem")[-1]

        if "problemset" in self.web_url:
            return problems_number.strip("/").split("/")[-1]
        else:
            return problems_number[1]

    def _get_contest_id(self) -> int:
        if "contest" in self.web_url:
            contest_number = self.web_url.split("contest")[1]
        elif "problemset" in self.web_url:
            contest_number = self.web_url.split("problem")[-1].strip("/").split("/")[0]
        else:
            logging.error("Cannot find contest or problemset")
            raise Exception("Cannot find contest or problemset")

        if "problem" in contest_number:
            contest_number = contest_number.split("problem")[0]

        contest_number = int(contest_number.strip("s/").strip("/"))

        return contest_number

    def _get_full_contest(self):
        all_contests = self._get_all_contests(self.contest_id)

        if len(all_contests) == 0:
            raise Exception("contest info was not found")

        return all_contests[0]

    def _get_all_contests(self, contest_id: int) -> List[Contest]:
        all_contests = requests.get('https://codeforces.com/api/contest.list?gym=false')
        all_contests = all_contests.json()["result"]
        all_contests = filter(lambda x: x["id"] == contest_id, all_contests)
        all_contests = list(map(lambda x: Contest(**x), all_contests))
        return all_contests

    # def get_sample_data(self) -> str:
    #     if not self.is_started or "problem" not in self.web_url:
    #         return ""
    #
    #     sample_data = self._web_content.select_one('.sample-test')
    #     sample_data = sample_data.select_one('.input > pre').contents
    #
    #     lines = []
    #
    #     for line in sample_data:
    #         if type(line) is Tag:
    #             if line.text != "":
    #                 lines.append(line.text)
    #         else:
    #             if line != "\n":
    #                 lines.append(line.text.strip("\n"))
    #
    #     return "\n".join(lines)

    def __str__(self):
        return f"""

|-------------------------------------------------------------------------------------------------------
|    CONTEST NAME: #{self.contest.name}
|
|    Divisions: {self.contest.divisions}
|    Contest: {self.contest_id}
|    
|    Problems:
|       - {list(map(lambda x: x.name, self.problems))}
|-------------------------------------------------------------------------------------------------------
        """


def modify_file(copy_to: Path, round_data: RoundData) -> None:
    for problem in round_data.problems:
        file_path = copy_to / f"{problem.number}.py"

        with open(file_path, 'r') as f:
            file_data = f.read()

        file_data = file_data.replace("CONTEST_NUMBER", str(round_data.contest.id))
        file_data = file_data.replace("PROBLEM_LETTER", str(problem.number[0]))
        file_data = file_data.replace("PROBLEM_TITLE", problem.name)
        file_data = file_data.replace("CODEFORCES_TAGS", str.join(", ", problem.tags))

        tags = []

        for division in round_data.contest.divisions:
            tags.append(f"tag-div-{division}")

        tags.append(f"tag-difficulty-{problem.rating}")

        file_data = file_data.replace("#tags#", str.join(", ", tags))

        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(file_data)


def copy_file_and_update_information(from_path: Path, copy_to: Path, round_data: RoundData) -> None:
    for problem in round_data.problems:
        if not path.isfile(copy_to / f"{problem.number}.py"):
            logger.info(f"Creating file: {problem.number}")
            shutil.copyfile(from_path, copy_to / f"{problem.number}.py")
        else:
            logging.error("File already created")

    modify_file(copy_to, round_data)


# def create_input_file(round_data: RoundData) -> None:
#     logger.info("Creating input file")
#
#     # clean input file for future
#     with open('input.txt', 'w') as f:
#         f.write(round_data.get_sample_data())


def get_folder_path(round_data: RoundData) -> Path:
    if "Global" in round_data.contest.name:
        folder_path = CURRENT_PATH / "_Global Rounds"
    elif "Educational" in round_data.contest.name:
        folder_path = CURRENT_PATH / "_Educational Rounds"
    elif "Codeforces Round" in round_data.contest.name or "Codeforces Beta Round" in round_data.contest.name:
        folder_path = CURRENT_PATH / "_Regular Rounds"
    else:
        folder_path = CURRENT_PATH / "_Special Rounds"

    return folder_path / round_data.contest.name


def get_template_file_path() -> Path:
    return CURRENT_PATH / "template.py"


def create_folder(folder_path: Path) -> None:
    logger.info(f"Creating folder: {folder_path}")

    try:
        mkdir(folder_path)
    except OSError:
        # continue because we can add new problem
        logging.warning("Folder already created")


def open_current_file(folder_path: Path, round_data: RoundData) -> None:
    if len(round_data.problems) != 0:
        problem = round_data.problems[0]
        file_path = folder_path / f"{problem.number}.py"
        webbrowser.open(str(file_path))


def generate_folder_with_problems() -> None:
    logger.info("Script started")

    WEB_URL = "https://codeforces.com/contests/1766"

    round_data = RoundData(WEB_URL, is_started=False)
    # round_data = RoundData(
    #     web_url="",
    #     contest_number="1747",
    #     round_number=828,
    #     division="3",
    #     is_started=False,
    # )

    folder_path = get_folder_path(round_data)
    create_folder(folder_path)
    template = get_template_file_path()
    # create_input_file(round_data)
    copy_file_and_update_information(template, folder_path, round_data)
    modify_file(folder_path, round_data)
    logger.error(round_data)
    open_current_file(folder_path, round_data)

    logger.info("Script ended")


if __name__ == "__main__":
    generate_folder_with_problems()
