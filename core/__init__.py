from core.advanced_shapes import *
from shapes.test_shapes import *

add_object(ColourSquare(Point(20, 20), 10), True, True, True)
add_object(Spaceship(Point(50, 50), 15, 0.2, 0.5, 8, 0.6), True, False, True)

loop()
