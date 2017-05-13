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


def test_shapes():
    """adds test shapes to window"""
    add_object(Maze(20, 10, Point(200, 200)))
    add_object(MazeSolver(Point(200, 200), 10), True)

# call test function
test_shapes()
# start loop and display window with parameter being frames per second
loop(20)
# ends program
quit()
