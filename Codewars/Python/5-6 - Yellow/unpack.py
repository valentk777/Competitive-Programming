# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/56ee74e7fd6a2c3c7800037e
# Notes  : tag-codewars, tag-kyu-6
# -----------------------------------------------------------

def unpack(listas):
    local = []
    for x in listas:
        t = type(x)
        if x is None or t == int or t == str or t == float:
            local.append(x)
        elif t == list or t == tuple or t == set:
            local.extend(x)
        elif t == dict:
            local.append(list(x.keys()))
            local.append(list(x.values()))
    if listas == local:
        return local
    else:
        return unpack(local)
