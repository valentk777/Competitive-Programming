# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/52742f58faf5485cae000b9a
# Notes  : tag-codewars
# -----------------------------------------------------------

def format_duration(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)
    result = []
    if y != 0:
        result.append(f"{y} year" if y == 1 else f"{y} years")
    if d != 0:
        result.append(f"{d} day" if d == 1 else f"{d} days")
    if h != 0:
        result.append(f"{h} hour" if h == 1 else f"{h} hours")
    if m != 0:
        result.append(f"{m} minute" if m == 1 else f"{m} minutes")
    if s != 0:
        result.append(f"{s} second" if s == 1 else f"{s} seconds")

    len_r = len(result)
    if len_r == 5:
        return f"{result[0]}, {result[1]}, {result[2]}, {result[3]} and {result[4]}"
    if len_r == 4:
        return f"{result[0]}, {result[1]}, {result[2]} and {result[3]}"
    if len_r == 3:
        return f"{result[0]}, {result[1]} and {result[2]}"
    elif len_r == 2:
        return f"{result[0]} and {result[1]}"
    elif len_r == 1:
        return result[0]
    else:
        return "now"
