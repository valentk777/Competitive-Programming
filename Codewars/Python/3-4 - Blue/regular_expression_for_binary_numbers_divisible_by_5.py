# -----------------------------------------------------------
# URL    : https://www.codewars.com/kata/5647c3858d4acbbe550000ad
# Notes  : tag-codewars, tag-kyu-4
# -----------------------------------------------------------


from greenery import fsm, lego

machine = fsm.fsm(
    alphabet={'0', '1'},
    states={'0', '1', '2', '3', '4'},
    initial='0',
    finals={'0'},
    map={
        '0': {'0': '0', '1': '1'},
        '1': {'0': '2', '1': '3'},
        '2': {'0': '4', '1': '0'},
        '3': {'0': '1', '1': '2'},
        '4': {'0': '3', '1': '4'},
    },
)

pattern = lego.from_fsm(machine)
print(pattern)
# (0|1(((0|1{2})(01*01)*01*0|1)0)*(0|1{2})(01*01)*1)*
