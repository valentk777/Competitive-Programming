def list_to_string(_a):
    return " ".join(map(str, _a))

# ----------------------------------------------------------------------
# range of chars from 'a' until 'z'
a = {chr(i): -1 for i in range(ord("a"), ord("z") + 1)}

# ----------------------------------------------------------------------
# used instead of dict. When we need to add value, it automatically add it with default value 0
from collections import defaultdict

x = defaultdict(int) 

x["test"] = 5
x["test_2"] += 1 # add +1 to value do not exist before. normal dict throw exception

# ----------------------------------------------------------------------
