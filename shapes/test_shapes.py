# ==============================================================================================================
# Python file containing test shapes used as examples in order to showcase the bare bones capability of the core
# ==============================================================================================================
# ColourSquare
# - - - - - -
# every tick the square's colour randomly changes to one of 6 present colours
# on key event the square will respond to 'w', 'a', 's' and 'd' as movement controls
# on click event square will teleport to mouse click position
# --------------------------------------------------------------------------------------------------------------
# Spaceship
# - - - - -
# the spaceship is a little more complicated...
# to find out more information on how it works look inside the class for more detailed comments
# to simplify things the space ship responds to the arrow keys as movement controls
# Left and Right rotate the triangle(spaceship) to face multiple directions
# Up will move the space ship forward in the direction it is facing
# the spaceship has inertia meaning it will keep going in that direction unless an opposite force is applied
# the Down key will slowly bring the spaceship to a stop no matter what direction is it currently facing
# --------------------------------------------------------------------------------------------------------------
# Face
# - -
# probably the simplest object which does not respond to any events
# the Face will simply be drawn at any size you want
# be prepared because my face drawing skill are horrible
# --------------------------------------------------------------------------------------------------------------
# Translator
# - - - - -
# the Translator simply translates an English phase into French
# to enable typing in it press Right Control, and to disable it press it again
# to translate a typed phrase press Enter
# more comments on how it actually works can be found in it's class
# ==============================================================================================================
from core.advanced_shapes import *
from libs.graphics import *
import random
import math
import urllib.request
import re


class ColourSquare(AdvancedShape):

    # based on parameters crates a rectangle and stores it
    def __init__(self, position, size):

        self.square = Rectangle(Point(position.getX() - size, position.getY() - size),
                                Point(position.getX() + size, position.getY() + size))

    # first draw  of object
    def display(self, window):
        self.square.draw(window)

    # every time key is pressed method will check for these keys and move square
    def key_event(self, key_event):
        if key_event == "w":
            self.square.move(0, -5)
        elif key_event == "a":
            self.square.move(-5, 0)
        elif key_event == "s":
            self.square.move(0, 5)
        elif key_event == "d":
            self.square.move(5, 0)

    # every time mouse is clicked, square is moved to mouse position
    def click_event(self, click_event):
        self.square.move(click_event.getX() - self.square.getCenter().getX(),
                         click_event.getY() - self.square.getCenter().getY())

    # every tick square colour is randomly set to one colour contained in the list
    def tick_event(self):
        self.square.setFill(random.choice(["blue", "red", "green", "yellow", "purple", "teal"]))


class Spaceship(AdvancedShape):

    # based on parameters it creates, calculates and stores different variables required for the Spaceship to work
    def __init__(self, position, size, acceleration=1, deceleration=2, rotate_speed=10, max_speed=5):
        self.speed_x = 0
        self.speed_y = 0
        self.rotate_speed = rotate_speed
        self.rotation = 0
        self.position = position
        self.size = size
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.max_speed = max_speed
        self.triangle = self._create_triangle()
        self.window = None

    # stores window because triangle must be manually redrawn every time it rotates
    def display(self, window):
        self.window = window
        self.triangle.draw(self.window)

    # checks if arrow key pressed and rotates it or through calculations decides how much the speed has to change
    def key_event(self, key_event):
        if key_event == "Left":
            self._rotate(-self.rotate_speed)
        elif key_event == "Right":
            self._rotate(self.rotate_speed)
        elif key_event == "Up":
            self.speed_x += min(math.cos(math.radians(self.rotation)) * self.acceleration, self.max_speed)
            self.speed_y += min(math.sin(math.radians(self.rotation)) * self.acceleration, self.max_speed)
        elif key_event == "Down":
            total_speed = abs(self.speed_x) + abs(self.speed_y) + 1
            self.speed_x -= self.speed_x / total_speed * self.deceleration
            self.speed_y -= self.speed_y / total_speed * self.deceleration

    # every tick updates triangle position based on movement direction
    def tick_event(self):
        self.triangle.move(self.speed_x, self.speed_y)
        self.position = Point(self.position.getX() + self.speed_x, self.position.getY() + self.speed_y)

    # lovely trigonometry to find 1 point of 1 axis of the triangle
    def _calculate_point_pos_cos(self, angle):
        return math.cos(math.radians(self.rotation + angle))*self.size

    # lovely trigonometry to find 1 point of 1 axis of the triangle
    def _calculate_point_pos_sin(self, angle):
        return math.sin(math.radians(self.rotation + angle))*self.size

    # uses the previous functions to generate 3 points that make up triangle from scratch
    def _create_triangle(self):
        return Polygon(Point(self.position.getX() + self._calculate_point_pos_cos(135),
                             self.position.getY() + self._calculate_point_pos_sin(135)),
                       Point(self.position.getX() + self._calculate_point_pos_cos(224),
                             self.position.getY() + self._calculate_point_pos_sin(224)),
                       Point(self.position.getX() + self._calculate_point_pos_cos(0),
                             self.position.getY() + self._calculate_point_pos_sin(0)))

    # deletes old triangle and re-creates a new one with new rotation and stores and draws it
    def _rotate(self, rotate_amount):
        self.rotation += rotate_amount
        self.triangle.undraw()
        self.triangle = self._create_triangle()
        self.triangle.draw(self.window)


class Face(AdvancedShape):

    # stores parameters and creates eyes separately in order to allow later implementation of eye movement
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.left_eye = Circle(Point(self.position.getX() - self.size / 4, self.position.getY() - self.size / 3), self.size / 15)
        self.right_eye = Circle(Point(self.position.getX() + self.size / 4, self.position.getY() - self.size / 3), self.size / 15)
        self.left_eye.setFill("black")
        self.right_eye.setFill("black")

    # creates the rest of the face and draws it
    def display(self, window):
        Circle(self.position, self.size).draw(window)
        Circle(Point(self.position.getX() - self.size / 4, self.position.getY() - self.size / 3), self.size / 6).draw(window)
        Circle(Point(self.position.getX() + self.size / 4, self.position.getY() - self.size / 3), self.size / 6).draw(window)
        Line(Point(self.position.getX() - self.size / 2, self.position.getY() + self.size / 3),
             Point(self.position.getX() + self.size / 2, self.position.getY() + self.size / 3)).draw(window)
        self.left_eye.draw(window)
        self.right_eye.draw(window)


class Translator(AdvancedShape):

    # creates and stores two Text objects, one for input and one for output
    def __init__(self, position, width):
        self.in_text = Text(Point(position.x, position.y + 10), "")
        self.out_text = Text(Point(position.x, position.y - 10), "Testing")
        self.selected = False

    # simply draws the Text
    def display(self, window):
        self.in_text.draw(window)
        self.out_text.draw(window)

    # checks if it is selected and then reacts accordingly by adding text ot input or translating
    def key_event(self, key_event):
        if key_event == "Control_L":
            self.selected = not self.selected
        if self.selected:
            if key_event == "Return":
                self.out_text.setText(self._translate(self.in_text.getText()))
            elif key_event == "BackSpace":
                self.in_text.setText(self.in_text.getText()[0:len(self.in_text.getText()) - 1])
            else:
                self.in_text.setText(self.in_text.getText() + self._key_parse(key_event))

    # method used to help convert words to symbols
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
            "underscore": "_",
        }
        if key_event in key_dict.keys():
            return key_dict.get(key_event)
        elif len(key_event) == 1:
            return key_event

        print("could not recognise: " + key_event)
        return "�"

    @staticmethod
    # 87.5% of class is copied (hence the copyright notice)
    # it basically goes to a simplified version of google translate and using the url inputs the text
    # it then reads the HTML page it receives and finds a specific div element that contains translation
    def _translate(text):
        """
        For some code used from https://github.com/mouuff/mtranslate/blob/master/mtranslate/core.py (plz don't sue me)
        MIT License
        Copyright (c) 2016 Arnaud Aliès
        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:
        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.
        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        """
        agent = {'User-Agent':
                     "Mozilla/4.0 (\
                     compatible;\
                     MSIE 6.0;\
                     Windows NT 5.1;\
                     SV1;\
                     .NET CLR 1.1.4322;\
                     .NET CLR 2.0.50727;\
                     .NET CLR 3.0.04506.30\
                     )"}

        request = urllib.request.Request(("http://translate.google.com/m?hl=fr&sl=en&q=" + text).replace(" ", "+"),
                                         headers=agent)
        raw_data = urllib.request.urlopen(request).read()

        data = raw_data.decode("utf-8")
        expr = r'class="t0">(.*?)<'
        re_result = re.findall(expr, data)
        return re_result[0]
