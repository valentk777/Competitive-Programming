import logging
import re
import shutil
from os import getcwd, mkdir, path
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Tag

logger = logging.getLogger()
logger.setLevel(1)

CURRENT_PATH = Path(getcwd())


class RoundData:
    def __init__(self, web_url, contest_number="", round_number=0, division="", is_started=True):
        self.web_url = web_url
        self._web_content = self._scrape_url(web_url) if web_url != "" else ""
        self.contest_number = self._get_contest_number() if contest_number == "" else contest_number
        self.round_number = self._get_round_number() if round_number == 0 else round_number
        self.division = self._get_division_number() if division == "" else division
        self.is_started = is_started
        self._problems = None

    def __str__(self):
        return f"""
        
|----------------------------------------------------------------------------------
|    ROUND: #{self.round_number}
|
|    Division: {self.division}
|    Contest: {self.contest_number}
|    
|    Problems:
|       - {list(map(lambda x: x[1], self._problems))}
|----------------------------------------------------------------------------------
        """

    def get_problems(self):
        if self._problems is not None:
            return self._problems

        if "problem" in self.web_url:
            problems_number = self.web_url.split("problem")[-1]

            if "problemset" in self.web_url:
                problems_number = problems_number.strip("/").split("/")[-1]
            else:
                problems_number = problems_number[1]
            problem_name = self._web_content.select_one(".problemindexholder").select_one(".title").text

            self._problems = [[problems_number.strip("/"), problem_name]]
            return self._problems

        result = []

        for i in range(ord("A"), ord("G") + 1):
            result.append([
                chr(i), self._get_problem_name(f"https://codeforces.com/contest/{self.contest_number}/problem/{chr(i)}")
            ])

        self._problems = result

        return self._problems

    def _get_contest_number(self) -> str:
        if "contest" in self.web_url:
            contest_number = self.web_url.split("contest")[1]
        elif "problemset" in self.web_url:
            contest_number = self.web_url.split("problem")[-1].strip("/").split("/")[0]
        else:
            logging.error("Cannot find contest or problemset")
            raise Exception("Cannot find contest or problemset")

        if "problem" in contest_number:
            contest_number = contest_number.split("problem")[0]

        contest_number = contest_number.strip("/")

        return contest_number

    def _get_round_number(self) -> int:
        select_round_section = self._web_content.select_one('.rtable').select_one(".left").text
        select_round_section = select_round_section.split("#")[1]
        round_number = re.findall(r'\d+', select_round_section)[0]
        return int(round_number)

    def _get_division_number(self) -> str:
        select_round_section = self._web_content.select_one('.rtable').select_one(".left").text

        if "Div." not in select_round_section:
            return "2"

        division_number = select_round_section.split("Div.")[1]
        division_number = re.findall(r'\d+', division_number)[0]

        return division_number

    def _get_problem_name(self, web_url: str) -> str:
        if not self.is_started:
            return "PROBLEM_NAME"

        try:
            web_content = self._scrape_url(web_url)
            problem_name = web_content.select_one(".problemindexholder").select_one(".title").text
        except:
            logger.error("Cannot find problem name")
            return "PROBLEM_NAME"

        return problem_name

    def _scrape_url(self, web_url) -> BeautifulSoup:
        r = requests.get(web_url)

        return BeautifulSoup(r.content, 'html.parser')

    def get_sample_data(self) -> str:
        if not self.is_started or "problem" not in self.web_url:
            return ""

        sample_data = self._web_content.select_one('.sample-test')
        sample_data = sample_data.select_one('.input > pre').contents

        lines = []

        for line in sample_data:
            if type(line) is Tag:
                if line.text != "":
                    lines.append(line.text)
            else:
                if line != "\n":
                    lines.append(line)

        return "\n".join(lines)


def modify_file(copy_to: Path, round_data: RoundData) -> None:
    for problem_file_path, name in round_data.get_problems():
        file_path = copy_to / f"{problem_file_path}.py"

        with open(file_path, 'r') as f:
            file_data = f.read()

        file_data = file_data.replace("CONTEST_NUMBER", round_data.contest_number)
        file_data = file_data.replace("PROBLEM_LETTER", file_path.name[0])
        file_data = file_data.replace("DIVISION", round_data.division)
        file_data = file_data.replace("PROBLEM_TITLE", name)

        with open(file_path, 'w') as f:
            f.write(file_data)


def copy_file_and_update_information(from_path: Path, copy_to: Path, round_data: RoundData) -> None:
    for problem_file_path, _ in round_data.get_problems():
        if not path.isfile(copy_to / f"{problem_file_path}.py"):
            logger.info(f"Creating file: {problem_file_path}")
            shutil.copyfile(from_path, copy_to / f"{problem_file_path}.py")
        else:
            logging.error("File already created")

    modify_file(copy_to, round_data)


def create_input_file(round_data: RoundData) -> None:
    logger.info("Creating input file")

    # clean input file for future
    with open('input.txt', 'w') as f:
        f.write(round_data.get_sample_data())


def get_folder_path(round_data: RoundData) -> Path:
    if round_data.round_number < 500:
        folder_path = CURRENT_PATH / "_Regular Rounds 1-499"
    else:
        folder_path = CURRENT_PATH / "_Regular Rounds 500-1000"

    folder_path = folder_path / f"Round #{round_data.round_number} (Div. {round_data.division})"

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


def generate_folder_with_problems() -> None:
    logger.info("Script started")

    WEB_URL = "https://codeforces.com/problemset/problem/50/A"

    round_data = RoundData(WEB_URL)
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
    create_input_file(round_data)
    copy_file_and_update_information(template, folder_path, round_data)
    modify_file(folder_path, round_data)
    logger.error(round_data)

    logger.info("Script ended")


if __name__ == "__main__":
    generate_folder_with_problems()
