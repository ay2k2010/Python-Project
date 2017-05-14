#test
from core.advanced_shapes import *
from libs.graphics import *

class InputTextField(AdvancedShape):
    pass
class Square(AdvancedShape):
    def __init__(self,position,size):
         self.square = Rectangle(Point(position.getX() - size, position.getY() - size),
                                Point(position.getX() + size, position.getY() + size))
    def display(self, window):
        self.square.draw(window)

