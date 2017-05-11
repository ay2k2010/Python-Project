# ==============================================================================================================
#              ▒█▀▀█ ▒█░▒█ ▒█▄░▒█ 　 ▀▀█▀▀ ▒█░▒█ ▀█▀ ▒█▀▀▀█ 　 ▒█▀▀▀ ▀█▀ ▒█░░░ ▒█▀▀▀
#              ▒█▄▄▀ ▒█░▒█ ▒█▒█▒█ 　 ░▒█░░ ▒█▀▀█ ▒█░ ░▀▀▀▄▄ 　 ▒█▀▀▀ ▒█░ ▒█░░░ ▒█▀▀▀
#              ▒█░▒█ ░▀▄▄▀ ▒█░░▀█ 　 ░▒█░░ ▒█░▒█ ▄█▄ ▒█▄▄▄█ 　 ▒█░░░ ▄█▄ ▒█▄▄█ ▒█▄▄▄
# ==============================================================================================================
# Python file that contains all of the initialization functions
# this is the file that must be run in order for the program to work
# it simply contains a test function that adds 3 test shapes to the program and then starts the loop
# ==============================================================================================================
from core.advanced_shapes import *
from shapes.test_shapes import *


def test_shapes():
    """adds test shapes to window"""
    # add_object(ColourSquare(Point(20, 20), 10), True, True, True)
    # add_object(Spaceship(Point(50, 50), 10, 0.1, 0.4, 8, 0.3), True, False, True)
    # add_object(Face(Point(150, 150), 25))
    add_object(Translator(Point(250, 250), 10), using_key_event=True)

# call test function
test_shapes()
# start loop and display window with parameter being frames per second
loop(20)
# ends program
quit()
