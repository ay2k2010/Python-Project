from core.advanced_shapes import *
from shapes.test_shapes import *


def test_shapes():
    add_object(ColourSquare(Point(20, 20), 10), True, True, True)
    add_object(Spaceship(Point(50, 50), 10, 0.1, 0.4, 8, 0.3), True, False, True)
    add_object(Face(Point(150, 150), 25))

test_shapes()
loop()
