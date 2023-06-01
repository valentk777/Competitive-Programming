import logging
import re
import shutil
import string
import webbrowser
from os import getcwd, mkdir, path
from pathlib import Path

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger()
logger.setLevel(1)

CURRENT_PATH = Path(getcwd())


class Problem:
    def __init__(self, web_url):
        self.web_url = web_url

        problem_info = self.get_problem_info()

        self.title = self._get_problem_title(problem_info)
        self.number = self._get_problem_number(problem_info)
        self.rating = self._get_problem_rating(problem_info)
        self.file_name = self._get_problem_filename()

    def get_problem_info(self) -> str:
        html = requests.get(self.web_url)
        problem_info = BeautifulSoup(html.text, "html.parser")
        problem_info = problem_info.contents[1].contents[1].contents[2].contents[0]

        return problem_info

    def _get_problem_title(self, problem_info: str) -> str:
        return re.findall(r"questionTitle\":\"([\w ]+)\"", problem_info)[0]

    def _get_problem_number(self, problem_info: str) -> str:
        return re.findall(r"questionId\":\"(\d+)\"", problem_info)[0]

    def _get_problem_rating(self, problem_info: str) -> str:
        return re.findall(r"difficulty\":\"(\w+)\"", problem_info)[0].lower()

    def _get_problem_filename(self):
        title = self.title.lower()
        translating = str.maketrans('', '', string.punctuation)
        title = title.translate(translating)
        title = title.replace(" ", "_")

        return f"{self.number}_{title}.py"


def modify_file(copy_to: Path, problem: Problem) -> None:
    file_path = copy_to / problem.file_name

    with open(file_path, 'r') as f:
        file_data = f.read()

    file_data = file_data.replace("PROBLEM_URL", problem.web_url)
    file_data = file_data.replace("PROBLEM_LETTER", problem.number)
    file_data = file_data.replace("PROBLEM_TITLE", f"{problem.number}. {problem.title}")
    # file_data = file_data.replace("LEETCODE_TAGS", str.join(", ", problem.tags))

    tags = []
    tags.append(f"tag-difficulty-{problem.rating}")

    file_data = file_data.replace("#tags#", str.join(", ", tags))

    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(file_data)


def copy_file_and_update_information(from_path: Path, copy_to: Path, problem: Problem) -> None:
    if not path.isfile(copy_to / problem.file_name):
        logger.info(f"Creating file: {problem.file_name}")
        shutil.copyfile(from_path, copy_to / problem.file_name)
    else:
        logging.error("File already created")

    modify_file(copy_to, problem)


# def create_input_file(round_data: RoundData) -> None:
#     logger.info("Creating input file")
#
#     # clean input file for future
#     with open('input.txt', 'w') as f:
#         f.write(round_data.get_sample_data())


def get_template_file_path() -> Path:
    return CURRENT_PATH / "template.py"


def create_folder(folder_path: Path) -> None:
    logger.info(f"Creating folder: {folder_path}")

    try:
        mkdir(folder_path)
    except OSError:
        # continue because we can add new problem
        logging.warning("Folder already created")


def open_current_file(folder_path: Path, problem: Problem) -> None:
    file_path = folder_path / problem.file_name
    webbrowser.open(str(file_path))


def generate_folder_with_problems() -> None:
    logger.info("Script started")

    WEB_URL = "https://leetcode.com/problems/product-of-array-except-self/"

    round_data = Problem(WEB_URL)

    folder_path = CURRENT_PATH / "Problems"
    template = get_template_file_path()
    copy_file_and_update_information(template, folder_path, round_data)
    modify_file(folder_path, round_data)
    logger.error(round_data)
    open_current_file(folder_path, round_data)

    logger.info("Script ended")


if __name__ == "__main__":
    generate_folder_with_problems()
