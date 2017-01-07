from core.advanced_shapes import *
from libs.graphics import *
import random


class ColourSquare(AdvancedShape):

    def __init__(self, position, size):

        self.square = Rectangle(Point(position.getX() - size, position.getY() - size),
                                Point(position.getX() + size, position.getY() + size))

    def display(self, window):
        self.square.draw(window)

    def key_event(self, key_event):
        if key_event == "w":
            self.square.move(0, -5)
        elif key_event == "a":
            self.square.move(-5, 0)
        elif key_event == "s":
            self.square.move(0, 5)
        elif key_event == "d":
            self.square.move(5, 0)

    def click_event(self, click_event):
        self.square.move(click_event.getX() - self.square.getCenter().getX(),
                         click_event.getY() - self.square.getCenter().getY())

    def tick_event(self):
        self.square.setFill(random.choice(["blue", "red", "green", "yellow", "purple", "teal"]))



