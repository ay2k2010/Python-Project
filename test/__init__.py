# Triangle Calculator:
#
#   A
#   |\
# a | \ c
#   |__\
#  B  b  C
import math
from decimal import *

def generate_string(char,num):
    return char * num

def process(var):
    return str(round(var, 2))

def cacl_amount_of_space(strBase, var, div):
    return strBase[0:max(0, int(len(strBase)-int(len(str(int(round(var*int(10**(abs(Decimal(process(var)).as_tuple().exponent))), 0))))/div)))]

def print_triangle():
    """prints the triangle with values"""
    str_base = generate_string(" ", max(3, len(process(a))+1))
    amount_of_lines = len(str(process(b)))+6
    inner_space_str = generate_string(" ", amount_of_lines)

    print(cacl_amount_of_space(str_base, A, 2) + process(A))
    for num in range(0, int((amount_of_lines/2))):
        print(str_base+"|"+inner_space_str[:num]+"\\")

    print(str(cacl_amount_of_space(str_base[0:2], a, 1)) + process(a) + " |" + inner_space_str[:int(amount_of_lines / 2)] + "\\ " + process(c))
    for num in range(int((amount_of_lines/2)+1), amount_of_lines):
        print(str_base + "|"+inner_space_str[:num]+"\\")

    print(str_base+"|"+generate_string("_", amount_of_lines)+"\\")
    print(cacl_amount_of_space(str_base, B, 1) + process(B) + "   " + process(b) + "   " + process(C))

    return


A = 10.1224213124
a = 13123.12312
B = 900.1231
b = 3.123123123
C = 123.12312
c = 123
# a = c*math.sin(A)
# a = b/math.tan(A)
print("Hello World")
print("Test")


print_triangle()