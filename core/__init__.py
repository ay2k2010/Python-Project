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
from shapes.maze_shapes import *
from shapes.input_shapes import *


def test_shapes():
    """adds test shapes to window"""
    add_object(Maze(35, 6, Point(320, 240)))
    add_object(MazeSolver(Point(320, 240), 6), True)
    # add_object(CoolRect(Point(400, 400), 40), True,)
    # add_object(InputTextField(Point(400, 400), 4), True)
    # add_object(CoolRect(Point(200, 400), 40), True, True)
    # add_object(InputTextField(Point(200, 400), 4), True)


# call test function
test_shapes()
# start loop and display window with parameter being frames per second
loop(20)
# ends program
quit()
