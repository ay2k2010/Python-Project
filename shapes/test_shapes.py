# THIS IS A TEST CLASS, ANYONE CAN ADD EXTRA SHAPES HERE TO TEST, OR CREATE A NEW DEDICATED FILE IN THIS PACKAGE
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
# ==============================================================================================================
from core.advanced_shapes import *
from libs.graphics import *
import random
import math


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

