#test
from core.advanced_shapes import *
from libs.graphics import *

class InputTextField(AdvancedShape):

    def __init__(self, position, width):
        self.in_text = Text(Point(position.getX(), position.getY() + 5), "")
        self.selected = False

    def key_event(self, key_event):
        if key_event == "Control_L":
            self.selected = not self.selected
        if self.selected:
            if key_event == "BackSpace":
                self.in_text.setText(self.in_text.getText()[0:len(self.in_text.getText()) - 1])
            else:
             self.in_text.setText(self.in_text.getText() + self._key_parse(key_event))
    @staticmethod
    def _key_parse(key_event):
        key_dict = {
            "Shift_L": "",
            "Shift_R": "",
            "Control_L": "",
            "Control_R": "",
            "Caps_Lock": "",
            "Delete": "",
            "Up": "",
            "Down": "",
            "Left": "",
            "Right": "",
            "space": " ",
            "period": ".",
            "comma": ",",
            "question": "?",
            "greater": ">",
            "less": "<",
            "semicolon": ";",
            "colon": ":",
            "quoteright": "'",
            "quoteleft": "'",
            "quotedbl": "\"",
            "backslash": "\\",
            "bar": "|",
            "asciitilde": "~",
            "exclam": "!",
            "at": "@",
            "numbersign": "#",
            "dollar": "$",
            "percent": "%",
            "asciicircum": "^",
            "asterisk": "*",
            "parenleft": "(",
            "parenright": ")",
            "minus": "-",
            "plus": "+",
            "equal": "=",
            "underscore": "_",}

    def display(self, window):
        self.in_text.draw(window)


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
