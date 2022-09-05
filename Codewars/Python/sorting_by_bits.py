# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/59fa8e2646d8433ee200003f
# Notes  : tag-codewars
# -----------------------------------------------------------

def sort_by_bit(arr):
    def to_string_bin(element):
        return bin(element).replace("0b", "")

    def count_number_of_ones(element):
        return len(list(filter(lambda x: x == '1', element)))

    binary = list(map(to_string_bin, arr))
    binary = list(map(count_number_of_ones, binary))
    x_sorted = sorted(zip(arr, binary), key=lambda x: (x[1], x[0]))
    res = list(map(lambda x: x[0], x_sorted))

    arr.clear()

    for e in res:
        arr.append(e)


# Blind4Basics solution
def sort_by_bit(arr):
    arr.sort(key=lambda n: (n.bit_count(), n))
