# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5e5acfe31b1c240012717a78
# Notes  : tag-codewars, tag-kyu-7
# -----------------------------------------------------------

def make_model_year(lst):
    new_dic = {"make": "", "model": "", "year": 0, "new": False, }
    for element in lst:
        if type(element) == int:
            new_dic["year"] = element
        elif type(element) == bool:
            new_dic["new"] = element
        elif type(element) == str:
            new_dic["make"] = element
        elif type(element) == tuple:
            new_dic["model"] = f"{element[0]} {element[1]}"
    return new_dic