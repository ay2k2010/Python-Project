#test
from core.advanced_shapes import *
from libs.graphics import *

class InputTextField(AdvancedShape):

    def __init__(self, position, width):
        self.in_text = Text(Point(position.getX(), position.getY() + 5), "")
        self.out_text = Text(Point(position.getX(), position.getY() - 5), "Enter Text")
        self.selected = False

    def key_event(self, key_event):
        if key_event == "Control_L":
            self.selected = not self.selected
        if self.selected:
            if key_event == "Return":
                self.out_text.setText(self.key_event(self.in_text.getText()))
            elif key_event == "BackSpace":
                self.in_text.setText(self.in_text.getText()[0:len(self.in_text.getText()) - 1])
            else:
                self.in_text.setText(self.in_text.getText() + self._key_parse(key_event))

    def display(self, window):
        self.in_text.draw(window)
        self.out_text.draw(window)


class CoolRect(AdvancedShape):
    def __init__(self,position,size):
         self.square = Rectangle(Point(position.getX() - size, position.getY() - size),
          Point(position.getX() + size, position.getY() + size))

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

    def display(self, window):
        self.square.draw(window)
