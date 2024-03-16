# ---------------------------------------------------------------------------------------
# URL    : https://programavimas.vgtu.lt/contests/55/problems/1986/
# Title  : Varžybos
# Tags   : tag-LSPO, tag-vgtu, tag-problem-J
# Notes  :
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------
import math
import sys
from collections import defaultdict, Counter

inp = lambda: sys.stdin.readline().strip().rstrip("\r\n")
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())
list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
flush = lambda: sys.stdout.flush()
print_flush = lambda _text: (print(_text), flush())
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = sys.maxsize
A = 911382323
M = 9999999999879998
# endregion
# -------------------------------------------------------Solution-------------------------------------------------------

MAN = {
    127: "Liudas",
    256: "Ignas",
    314: "Povilas",
    362: "Rapolas",
    405: "Mindaugas",
    434: "Lukas",
    435: "Vytautas",
    475: "Rytis",
    513: "Karolis",
    518: "Modestas",
    525: "Kostas",
    529: "Rimas",
    607: "Saulius",
    618: "Jurgis",
    628: "Gytis",
    629: "Algirdas",
    643: "Mykolas",
    686: "Tomas",
    702: "Algis",
    739: "Antanas",
    741: "Eimantas",
    867: "Rimantas",
    875: "Albinas",
    894: "Petras",
    919: "Mantas",
}

WOMAN = {
    125: "Neringa",
    165: "Rasa",
    220: "Monika",
    234: "Ona",
    268: "Inesa",
    280: "Irina",
    327: "Greta",
    357: "Aleksandra",
    464: "Karolina",
    484: "Odeta",
    501: "Vaida",
    555: "Daiva",
    598: "Simona",
    634: "Elvyra",
    707: "Ligita",
    720: "Jurgita",
    763: "Veronika",
    783: "Eva",
    795: "Ieva",
    821: "Raimonda",
    828: "Brigita",
    848: "Aldona",
    884: "Rosita",
    943: "Renata",
    992: "Kotryna",
}

def solve():
    n = iinp()

    for m_key, m_value in MAN.items():
        for w_key, w_value in WOMAN.items():
            _sum = m_key + w_key

            if _sum == n:
                return f"{w_value} {m_value}"

            if _sum > n:
                break

    return "klaida"


def run():
    print(solve())


if __name__ == "__main__":
    run()



