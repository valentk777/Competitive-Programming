# -----------------------------------------------------------
#
# https://www.codewars.com/kata/515decfd9dcfc23bb6000006
#
# -----------------------------------------------------------

def is_valid_IP(string: str) -> bool:
    list_to_validate = string.split(".")

    if len(list_to_validate) != 4:
        return False

    for number in list_to_validate:
        if not number.isdigit() or int(number) > 255 or int(number) < 0 or number[0] == "0" and int(number) != 0:
            return False

    return True
