# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/515e188a311df01cba000003
# Notes  : tag-codewars, tag-kyu-8
# -----------------------------------------------------------

def get_planet_name(switcher_id: int) -> str:
    switcher = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    return switcher.get(switcher_id)