# Triangle Calculator:
#
#   A
#   |\
# a | \ c
#   |__\
#  B  b  C
import math
from decimal import *
def process(var):
    return str(round(var, 2))

def caclamountofspace( strBase, var, div):
    return strBase[0:max(0, int(len(strBase)-int(len(str(int(round(var*int(10**(abs(Decimal(process(var)).as_tuple().exponent))), 0))))/div)))]

def printtriangle():
    """prints the triangle with values"""
    strBaseOrginal = "                                                                                                        "
    strBase = strBaseOrginal[0:max(3, len(process(a))+1)]
    amountOfLines = len(str(float(process(b))+2-1))
    print(amountOfLines)

    print(caclamountofspace(strBase, A, 2) + process(A))
    for num in range(0, int((amountOfLines/2))):
        print(strBase+"|"+strBaseOrginal[0:num]+"\\")

    print(str(caclamountofspace(strBase[0:2], a, 1)) + process(a) + " |"+str(strBaseOrginal[0:int(amountOfLines/2)])+"\\ " + process(c))
    for num in range(int((amountOfLines/2)+1), amountOfLines):
        print(strBase + "|"+strBaseOrginal[0:num]+"\\")

    print(strBase+"|__\\")

    print(caclamountofspace(strBase, B, 1) + process(B) + " " + process(b) + " " + process(C))
    return


A = 10.1224213124
a = 1
B = 900
b = 1241342.123123123
b = 1241342.123123123
C = 0
c = 0
# a = c*math.sin(A)
# a = b/math.tan(A)
print("Hello World")
print("Test")


printtriangle()