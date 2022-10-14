import logging
import shutil
from os import getcwd, mkdir, path
from pathlib import Path
from typing import List

logger = logging.getLogger()
logger.setLevel(1)

CURRENT_PATH = Path(getcwd())
WEB_URL = "https://codeforces.com/contest/1742/problem/A"


class RoundData:
    def __init__(self, web_url):
        self.web_url = web_url
        self.contest_number = self._get_contest_number()
        self.round_number = self._get_round_number()
        self.division = self._get_division_number()
        self.problems = self._get_problems()

    def _get_contest_number(self) -> int:
        contest_number = self.web_url.split("contest")[1]

        if "problem" in contest_number:
            contest_number = contest_number.split("problem")[0]

        contest_number = contest_number.strip("/")

        return int(contest_number)

    def _get_round_number(self) -> str:
        return "1"

    def _get_division_number(self) -> str:
        return 2

    def _get_problems(self):
        if "problem" in self.web_url:
            problems_number = self.web_url.split("problem")[1]
            return [problems_number.strip("/")]

        return [chr(i) for i in range(ord("A"), ord("G") + 1)]


def modify_file(file_path: Path, round_data: RoundData) -> None:
    with open(file_path, 'r') as f:
        file_data = f.read()

    file_data = file_data.replace("ROUND_NUMBER", round_data.round_number)
    file_data = file_data.replace("PROBLEM_LETTER", file_path.name[0])
    file_data = file_data.replace("DIVISION", round_data.division)

    with open(file_path, 'w') as f:
        f.write(file_data)


def get_paths_for_problems_to_create(to_path: Path, problem_letter: str = None) -> List[Path]:
    if problem_letter is not None:
        problem_file_path = to_path / f"{problem_letter}.py"
        return [problem_file_path]

    problems_to_create = []

    for i in range(ord("A"), ord("G") + 1):
        problem_file_path = to_path / f"{chr(i)}.py"
        problems_to_create.append(problem_file_path)

    return problems_to_create


def copy_file_and_update_information(from_path: Path, problems_to_create: List[Path], round_data: RoundData) -> None:
    for problem_file_path in problems_to_create:

        if not path.isfile(problem_file_path):
            logger.info(f"Creating file: {problem_file_path}")
            shutil.copyfile(from_path, problem_file_path)
            modify_file(problem_file_path, round_data)
        else:
            logging.error("File already created")


def create_input_file():
    logger.info("Creating input file")

    with open('input.txt', 'a') as f:
        f.write('')


def get_folder_path(round_data: RoundData) -> Path:
    if round_data.contest_number < 500:
        folder_path = CURRENT_PATH / "_Regular Rounds 1-499"
    else:
        folder_path = CURRENT_PATH / "_Regular Rounds 500-1000"

    folder_path = folder_path / f"Round #{round_data.contest_number} (Div. {round_data.division})"

    return folder_path


def get_template_file_path() -> Path:
    return CURRENT_PATH / "template.py"


def create_folder(folder_path: Path) -> None:
    logger.info(f"Creating folder: {folder_path}")

    try:
        mkdir(folder_path)
    except OSError:
        # continue because we can add new problem
        logging.warning("Folder already created")


def generate_folder_with_problems(problem_letter: str = None) -> None:
    logger.info("Script started")

    round_data = RoundData(WEB_URL)
    folder_path = get_folder_path(round_data)
    create_folder(folder_path)
    template = get_template_file_path()
    create_input_file()
    problems_to_create = get_paths_for_problems_to_create(folder_path, problem_letter)
    copy_file_and_update_information(template, problems_to_create, round_data)

    logger.info("Script ended")


if __name__ == "__main__":
    generate_folder_with_problems()
