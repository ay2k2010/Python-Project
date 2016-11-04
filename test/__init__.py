# Triangle Calculator:
#
#   A
#   |\
# b | \ c
#   |__\
#  C  a  B
amount_of_decimal_places = 2


import math
import sys
from decimal import *


def simplify_number(num):
    """converts floats with no decimal places to ints"""
    if float(num).is_integer():
        return int(num)
    return num


def generate_string(char, num):
    """creates a string of characters of a certain length"""
    return char * num


def process(var):
    """rounds number and converts to string"""
    return str(round(var, amount_of_decimal_places))


def cacl_amount_of_space(str_base, var, div):
    """calculates the amount of space before a value un order for its position to stay fixed relative to the triangle"""
    return str_base[0:max(0, int(len(str_base) - int(len(str(int(round(var * int(10 ** (abs(Decimal(process(var)).as_tuple().exponent))), 0)))) / div)))]


def print_triangle():
    """prints the triangle with values"""
    str_base = generate_string(" ", max(3, len(process(b))+1))
    amount_of_lines = len(str(process(a)))+6
    inner_space_str = generate_string(" ", amount_of_lines)

    print(cacl_amount_of_space(str_base, A, 2) + process(A))

    for num in range(0, int((amount_of_lines/2))):
        print(str_base+"|"+inner_space_str[:num]+"\\")

    print(str(cacl_amount_of_space(str_base[0:2], a, 1)) + process(b) + " |" + inner_space_str[:int(amount_of_lines / 2)] + "\\ " + process(c))

    for num in range(int((amount_of_lines/2)+1), amount_of_lines):
        print(str_base + "|"+inner_space_str[:num]+"\\")

    print(str_base+"|"+generate_string("_", amount_of_lines)+"\\")
    print(cacl_amount_of_space(str_base, C, 1) + process(C) + "    " + process(a) + "    " + process(B))

    return
#
#
#
A = 0
a = 0
B = 90
b = 0
C = 0
c = 0
# a = c*math.sin(A)
# a = b/math.tan(A)


def solve_triangle(values):
    """calculates the missing value of the triangle"""
    value_keys = list(values.keys())
    angle_names = ["A", "B", "C"]
    side_names = ["a", "b", "c"]
    solved_angles = {"C": 90}
    solved_sides = {}

    def define_variable(var, value):
        globals()[var] = value
        if key in angle_names:
            nonlocal solved_angles
            solved_angles[key] = key_value
        elif key in side_names:
            nonlocal solved_sides
            solved_sides[key] = key_value
        else:
            # stops program
            sys.exit("\'" + key + "\' is not a valid variable name")

    # define methods for multiple calls
    def finish_angle_solve():
        key_list = list(solved_angles.keys())
        for var in angle_names:
            if var not in solved_angles:
                define_variable(var, solved_angles.get(key_list[0]) - solved_angles.get(key_list[1]))

    def finish_side_solve():
        key_list = list(solved_sides.keys())
        for var in side_names:
            if var not in solved_sides:
                if var is "c":
                    define_variable(var, simplify_number(math.sqrt(solved_sides.get(key_list[0])**2 + solved_sides.get(key_list[1])**2)))
                else:
                    define_variable(var, simplify_number(math.sqrt(abs(solved_sides.get(key_list[0])**2 - solved_sides.get(key_list[1])**2))))

    def solve_side_with_angles():
        print("")

    def solve_angle_with_sides():
        for var in angle_names:
            if var not in solved_angles:
                define_variable(var, math.sin(globals()[var.lower()]/globals()["c"]))

    # checks to see if info given is valid
    for key in values:
        key_value = values.get(key)
        if key is "C" and key_value is not 90:
            # stops program
            sys.exit("C is a right angle and cannot be set to anything that is not its default: 90")
        else:
            define_variable(key, key_value)

    # solving logic
    if len(solved_angles) is 2:
        finish_angle_solve()
    if len(solved_sides) is 2:
        finish_side_solve()
        if len(solved_angles) is 1:
            solve_angle_with_sides()
            finish_angle_solve()


solve_triangle({"b": 4, "c": 5})
print_triangle()
