# --------------------------------------------- #

# Triangle Calculator:
#
#   A
#   |\
# b | \ c
#   |__\
#  C  a  B
#
# Setup:
#
# set the angles or sides based on their letter
# C is already set to 90 (right angle)
values_dict = {
    "c": 5,
    "A": 36.869898,
}
#
# set amount of decimal places in answers
amount_of_decimal_places = 2
#
# --------------------------------------------- #

import math
import sys
import time
from decimal import *

# start timer
start_time = time.time()


def generate_string(char, num):
    """creates a string of characters of a certain length"""
    return char * num


def process(var):
    """rounds number and converts to string"""
    simplified = float(str('%f' % round(float(var), amount_of_decimal_places)).rstrip('0').rstrip('.'))
    if simplified.is_integer():
        return int(simplified)
    else:
        return simplified


def cacl_amount_of_space(str_base, var, div):
    """calculates the amount of space before a value un order for its position to stay fixed relative to the triangle"""
    return str_base[0:max(0, int(len(str_base) - int(len(str(int(round(float(var) * int(10 ** (abs(Decimal(process(var)).as_tuple().exponent))), 0)))) / div)))]


def print_triangle():
    """prints the triangle with values"""
    str_base = generate_string(" ", max(3, len(str(b))+1))
    amount_of_lines = len(str(a))+6
    inner_space_str = generate_string(" ", amount_of_lines)

    print(cacl_amount_of_space(str_base, A, 2) + str(A))

    for num in range(0, int((amount_of_lines/2))):
        print(str_base+"|"+inner_space_str[:num]+"\\")

    print(str(cacl_amount_of_space(str_base[0:2], a, 1)) + str(b) + " |" + inner_space_str[:int(amount_of_lines / 2)] + "\\ " + str(c))

    for num in range(int((amount_of_lines/2)+1), amount_of_lines):
        print(str_base + "|"+inner_space_str[:num]+"\\")

    print(str_base+"|"+generate_string("_", amount_of_lines)+"\\")
    print(cacl_amount_of_space(str_base, C, 1) + str(C) + "    " + str(a) + "    " + str(B))

    return
#
#
#
A = 0
a = 0
B = 0
b = 0
C = 90
c = 0
# a = c*math.sin(A)
# a = b/math.tan(A)


def solve_triangle(values):
    """calculates the missing value of the triangle"""
    angle_names = ["C", "B", "A"]
    side_names = ["c", "b", "a"]
    solved_angles = {"C": 90}
    solved_sides = {}

    def define_variable(var, value):
        globals()[var] = value
        if var in angle_names:
            solved_angles[var] = value
        elif var in side_names:
            solved_sides[var] = value
        else:
            # stops program
            sys.exit("'" + key + "' is not a valid variable name")

    # define methods for multiple calls
    def finish_angle_solve():
        key_list = list(solved_angles.keys())
        for var in angle_names:
            if var not in solved_angles:
                define_variable(var, abs(solved_angles.get(key_list[0]) - solved_angles.get(key_list[1])))

    def finish_side_solve():
        key_list = list(solved_sides.keys())
        for var in side_names:
            if var not in solved_sides:
                if var is "c":
                    define_variable(var, math.sqrt(solved_sides.get(key_list[0])**2 + solved_sides.get(key_list[1])**2))
                else:
                    define_variable(var, math.sqrt(abs(solved_sides.get(key_list[0])**2 - solved_sides.get(key_list[1])**2)))

    def solve_sides_with_angles():
        key_list = list(solved_sides.keys())
        for var in side_names:
            if var not in solved_sides:
                if var is "c":
                    define_variable(var, solved_sides.get(key_list[0]) / math.sin(math.radians(globals()[key_list[0].upper()])))
                else:
                    define_variable(var, globals()["c"] * math.sin(math.radians(globals()[var.upper()])))

    def solve_angles_with_sides():
        for var in angle_names:
            if var not in solved_angles:
                define_variable(var, math.degrees(math.asin(globals()[var.lower()]/globals()["c"])))

    # checks to see if info given is valid
    for key in values:
        key_value = values.get(key)
        if key is "C" and key_value is not 90:
            # stops program
            sys.exit("C is a right angle and cannot be set to anything that is not its default: 90")
        else:
            define_variable(key, key_value)

    # extra validation
    if "c" in solved_sides:
        key_list = list(solved_sides.keys())
        for var in solved_sides:
            if var is not "c" and solved_sides.get(var) > solved_sides.get(key_list[key_list.index("c")]):
                sys.exit("('" + var + "' = " + str(solved_sides.get(var)) + ") cannot be greater than the hypotenuse: ('c' = " + str(solved_sides.get(key_list[key_list.index("c")])) + ")")

    # solving logic
    if len(solved_angles) is 2:
        finish_angle_solve()
    if len(solved_angles) is 3:
        if len(solved_sides) <= 2:
            solve_sides_with_angles()
    if len(solved_sides) is 2:
        finish_side_solve()
    if len(solved_sides) is 3:
        if len(solved_angles) <= 2:
            solve_angles_with_sides()

    for var in solved_angles:
        globals()[var] = process(solved_angles.get(var))
    for var in solved_sides:
        globals()[var] = process(solved_sides.get(var))

solve_triangle(values_dict)
print_triangle()
print("Execution took: %s seconds" % (time.time() - start_time))
