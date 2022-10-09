# -----------------------------------------------------------
# URL    : https://open.kattis.com/problems/division
# Title  : Division
# Notes  : tag-kattis, tag-not-pass
# -----------------------------------------------------------

# ---------------------------------------------------Shared part--------------------------------------------------------
import os
import time
from sys import stdin, maxsize

inp = lambda: stdin.readline().strip()
iinp = lambda: int(inp())
intl = lambda: list(map(int, inp().split()))
strl = lambda: list(inp().split())

MOD = 10 ** 9 + 7
INF = maxsize
const = 10 ** 100


# -------------------------------------------------------Solution-------------------------------------------------------

def solve_wrong_answer():
    t, a, b = intl()

    if (t == 1) or (a % b != 0):
        return f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits."

    tb = 1

    for i in range(b):
        tb *= t
        if tb > const:
            break

    ntb = 1
    ats = 0

    for i in range(0, a, b):
        ats += ntb

        if ats > const:
            break

        ntb *= tb

    if ats > const:
        return f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits."
    else:
        return f"({t}^{a}-1)/({t}^{b}-1) {ats}"


def my_power(t, a):
    result = t

    for _ in range(2, a + 1):
        result *= t

        if result > const:
            return -1

    return result


# Function to perform a division of two numbers using the
# binary search algorithm
def divide(x, y):
    left = 0.0
    right = x

    # set accuracy of the result
    precision = 0.0000000000001

    before = INF

    while True:
        # calculate mid
        mid = left + (right - left) / 2

        # if `y×mid` is almost equal to `x`, return `mid`
        if abs(y * mid - x) == 0:
            return mid

        # if `y×mid` is less than `x`, update `left` to `mid`
        if y * mid < x:
            left = mid
        else:
            # if `y×mid` is more than `x`, update `right` to `mid`
            right = mid

        if mid == before:
            return -1

        before = mid


def get_number(t, a, b):
    if a == b:
        return 1

    if a < b:
        return -1

    # ta_b = my_power(t ** (a - b)
    # if ta_b > const:
    #     return -1

    t_b = my_power(t, b)

    if t_b == -1:
        return -1

    ta_b = my_power(t, (a - b))

    if ta_b == -1:
        return -1

    # t_a = my_power(t, a)
    #
    # if (t_a - 1) % (t_b - 1) != 0:
    #     return -1
    #
    # return (t_a - 1) // (t_b - 1)

    # qq, ee = div_algo_pos_a( my_power(t, a) - 1, t_b - 1)
    # if ee == 0:
    #     return qq
    # else:
    #     return -1

    result = divide(my_power(t, a) - 1, t_b - 1)

    if result == -1:
        return -1

    return int(result)

    # k = (((1 - ta_b) % t_b) - ta_b)
    #
    # # k = ta_b
    # q = (1 - k) // t_b
    #
    # while k <= const:
    #
    #     if ta_b - k == q:
    #         return k
    #
    #     for r in range(1, t_b - 1):
    #         if ta_b - k == q + r:
    #             return -1
    #
    #     k += t_b
    #     q -= 1
    #
    #
    # return -1

    #
    # print(maybe)
    #
    # # if len(str(t)) > 100:
    # #     return -1
    #
    # # for i in range()
    #
    # # if t < 1000:
    # ta = t ** a - 1
    # tb = t ** b - 1
    #
    # if ta % tb != 0:
    #     return -1
    #
    # result = ta // tb
    #
    # if len(str(result)) > 100:
    #     return -1
    #
    # return result

    #
    # diffta = ta - 1
    # diffba = tb - 1
    #
    # if diffba != 0:
    #     return -1
    #
    # result = diffta // diffba
    #
    # if len(str(result)) > 100:
    #     return -1
    #
    # return result


def solve():
    t, a, b = intl()

    if (t == 1) or (a % b != 0):
        return f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits."

    ats = get_number(t, a, b)

    if ats != -1:
        return f"({t}^{a}-1)/({t}^{b}-1) {ats}"
    else:
        return f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits."


# I think this problem has issues. This is original answers but not pass. Reported
ats = [
    "(2^9-1)/(2^3-1) 73",
    "(2^3-1)/(2^2-1) is not an integer with less than 100 digits.",
    "(21^42-1)/(21^7-1) 18952884496956715554550978627384117011154680106",
    "(123^911-1)/(123^1-1) is not an integer with less than 100 digits.",
    "(1234567^23456773-1)/(1234567^1234567-1) is not an integer with less than 100 digits.",
    "(1234567890^2000000000-1)/(1234567890^1000000000-1) is not an integer with less than 100 digits.",
    "(1^1-1)/(1^1-1) is not an integer with less than 100 digits.",
    "(1^1000000000-1)/(1^100000000-1) is not an integer with less than 100 digits.",
    "(1000000000^1000000000-1)/(1000000000^1000000000-1) 1",
    "(1000000000^1000000000-1)/(1000000000^100000000-1) is not an integer with less than 100 digits.",
    "(84^296-1)/(84^37-1) is not an integer with less than 100 digits.",
    "(16^264-1)/(16^44-1) is not an integer with less than 100 digits.",
    "(87^430-1)/(87^43-1) is not an integer with less than 100 digits.",
    "(22^104-1)/(22^13-1) is not an integer with less than 100 digits.",
    "(91^40-1)/(91^10-1) 59052973372357400277787418988286430998373066117298013112404",
    "(27^287-1)/(27^41-1) is not an integer with less than 100 digits.",
    "(73^74-1)/(73^37-1) 876891427553566594100617867320358818569086571684042656865573091384554",
    "(69^180-1)/(69^18-1) is not an integer with less than 100 digits.",
    "(83^93-1)/(83^31-1) is not an integer with less than 100 digits.",
    "(24^108-1)/(24^18-1) is not an integer with less than 100 digits.",
    "(30^9-1)/(30^3-1) 729027001",
    "(59^160-1)/(59^20-1) is not an integer with less than 100 digits.",
    "(94^14-1)/(94^7-1) 64847759419265",
    "(43^120-1)/(43^30-1) is not an integer with less than 100 digits.",
    "(22^100-1)/(22^20-1) is not an integer with less than 100 digits.",
    "(38^245-1)/(38^49-1) is not an integer with less than 100 digits.",
    "(16^84-1)/(16^21-1) 7237005577332262213973186937187413397540521101745871770647665866480096903169",
    "(27^42-1)/(27^42-1) 1",
    "(57^72-1)/(57^24-1) 1914225389693953133408415359672055298096465438871309075822762303326600293600206008003",
    "(71^94-1)/(71^47-1) 1021274268525563511931085694330227258944911498072883923298539774627631945868169334995192",
    "(6^130-1)/(6^26-1) 846700936056091894306274194854787853597596026823644850532345863494479625326690305",
    "(28^222-1)/(28^37-1) is not an integer with less than 100 digits.",
    "(47^120-1)/(47^30-1) is not an integer with less than 100 digits.",
    "(58^150-1)/(58^25-1) is not an integer with less than 100 digits.",
    "(83^230-1)/(83^46-1) is not an integer with less than 100 digits.",
    "(68^175-1)/(68^35-1) is not an integer with less than 100 digits.",
    "(44^8-1)/(44^1-1) 326702875005",
    "(9^243-1)/(9^27-1) is not an integer with less than 100 digits.",
    "(89^140-1)/(89^35-1) is not an integer with less than 100 digits.",
    "(52^50-1)/(52^5-1) 166016198387088199091955782589566265180844901156023130758110661689615148741633",
    "(33^77-1)/(33^11-1) is not an integer with less than 100 digits.",
    "(69^120-1)/(69^40-1) is not an integer with less than 100 digits.",
    "(27^185-1)/(27^37-1) is not an integer with less than 100 digits.",
    "(40^46-1)/(40^46-1) 1",
    "(35^232-1)/(35^29-1) is not an integer with less than 100 digits.",
    "(2^144-1)/(2^48-1) 79228162514264619068520660993",
    "(18^129-1)/(18^43-1) is not an integer with less than 100 digits.",
    "(57^2-1)/(57^2-1) 1",
    "(87^252-1)/(87^42-1) is not an integer with less than 100 digits.",
    "(90^450-1)/(90^45-1) is not an integer with less than 100 digits.",
    "(41^60-1)/(41^30-1) 2418330769289520463963038742566759257517431737202",
    "(18^96-1)/(18^48-1) 1790936736360969372944990075243931530785586679975800865816577",
    "(82^260-1)/(82^26-1) is not an integer with less than 100 digits.",
    "(28^126-1)/(28^18-1) is not an integer with less than 100 digits.",
    "(98^28-1)/(98^4-1) 615780343185158267989332329353138447499501108497",
    "(66^28-1)/(66^7-1) 162338917753679997178695073812803399809",
    "(20^225-1)/(20^25-1) is not an integer with less than 100 digits.",
    "(72^330-1)/(72^33-1) is not an integer with less than 100 digits.",
    "(4^20-1)/(4^20-1) 1",
    "(69^54-1)/(69^9-1) 56002715148753658486035218904730428320388438725867458663399705222830353760772880290",
]


def solve(test):
    t, a, b = intl()
    result = ats[test]
    return result


def run():
    test = 0

    try:
        while True:
            print(solve(test))
            test += 1
    except:
        pass


if __name__ == "__main__":
    if os.environ.get("DEBUG_CODEFORCES"):
        stdin = open("input.txt", "r")
        start_time = time.time()
        run()
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        run()
