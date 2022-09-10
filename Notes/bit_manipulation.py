import random

# just pick random numbers
x = random.randint(2 ** 2, 2 ** 3 + 1)
print(f"x = {x}")
print(f"bin x = {bin(x)}")

# # AND operation
is_number_even = x & 1 == 0
print(f"is_number_even = {is_number_even}")

is_number_odd = x & 1 == 1
print(f"is_number_odd = {is_number_odd}")

# is number divisible by 2^k
k = 3
is_number_divisible_by_2k = x & (2 ** k - 1) == 0
print(f"is_number_divisible_by_2k = {is_number_divisible_by_2k}")

# set last bit 1 in binary to 0, not last bit representation number
# ex: 110 -> 100
set_last_one_bit_to_zero = x & (x - 1)
print(f"bin set_last_one_bit_to_zero = {bin(set_last_one_bit_to_zero)}")

is_power_of_two = set_last_one_bit_to_zero == 0
print(f"is_power_of_two = {is_power_of_two}")

set_all_one_bits_to_zero_except_the_last_one = x & -x
print(f"bin set_all_one_bits_to_zero_except_the_last_one = {bin(set_all_one_bits_to_zero_except_the_last_one)}")

# # OR operation
invert_all_bits_after_the_last_one = x | (x - 1)
print(f"bin invert_all_bits_after_the_last_one = {bin(invert_all_bits_after_the_last_one)}")

# # XOR operation
# always return 0
print(f"x ^ x = {bin(x ^ x)}")

# all to 1: 101 -> 111; 1000 -> 1111
print(f"x ^ 1 = {bin(x ^ 1)}")

# do nothing: x ^ 0 = x
print(f"x ^ 0 = {bin(x ^ 0)}")

# NOT operation
# formula ~x == -x -1
#  29 -> 000000000000000000011101
# -30 -> 111111111111111111100010
inverted_x = ~x
print(f"~x == -x - 1 -> {~x == -x - 1}")
print(f"inverted_x = {inverted_x}")
print(f"bin inverted_x = {bin(inverted_x)}")

# # bit shift
# left bit shift x << k append k zero bit to the number
# same as multiplying x by 2^k -> x << k == x * 2**k
print(f"x << k == x * 2**k -> {x << k == x * 2 ** k}")

# right bit shift x >> k removes k bits from the number
# same as dividing x by 2^k and rounded down to integer -> x >> k == x // 2**k
print(f"x >> k == x // 2**k -> {x >> k == x // 2 ** k}")

# # bit mask
# used to access specific bits
mask = 1 << k  # return 1 only in k-th bit. others will be 0
print(f"mask = {mask}")
# get k-th bit of number x

print(f"bin x & mask = {bin(x & mask)}")

# set k-th bit to 1
print(f"bin set k-th bit to 1 = {bin(x | mask)}")

# set k-th bit to 0
print(f"bin set k-th bit to 0 = {bin(x & ~mask)}")

# invert k-th bit
print(f"bin set k-th bit to 0 = {bin(x ^ mask)}")



# functions
x.bit_length()
x.bit_count()
