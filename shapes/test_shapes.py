from core.advanced_shapes import *
from libs.graphics import *
import random
import math

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

class Spaceship(AdvancedShape):

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

    def display(self, window):
        self.window = window
        self.triangle.draw(self.window)

    def key_event(self, key_event):
        if key_event == "Left":
            self._rotate(-self.rotate_speed)
        elif key_event == "Right":
            self._rotate(self.rotate_speed)
        elif key_event == "Up":
            self.speed_x += min(math.cos(math.radians(self.rotation)) * self.acceleration, self.max_speed)
            self.speed_y += min(math.sin(math.radians(self.rotation)) * self.acceleration, self.max_speed)
        elif key_event == "Down":
            abs_speed_x = abs(self.speed_x)
            abs_speed_y = abs(self.speed_y)
            total_speed = abs_speed_x + abs_speed_y + 1
            self.speed_x -= self.speed_x / total_speed * self.deceleration
            self.speed_y -= self.speed_y / total_speed * self.deceleration

    def tick_event(self):
        self.triangle.move(self.speed_x, self.speed_y)
        self.position = Point(self.position.getX() + self.speed_x, self.position.getY() + self.speed_y)

    def _calculate_point_pos_cos(self, angle):
        return math.cos(math.radians(self.rotation + angle))*self.size

    def _calculate_point_pos_sin(self, angle):
        return math.sin(math.radians(self.rotation + angle))*self.size

    def _create_triangle(self):
        return Polygon(Point(self.position.getX() + self._calculate_point_pos_cos(135),
                             self.position.getY() + self._calculate_point_pos_sin(135)),
                       Point(self.position.getX() + self._calculate_point_pos_cos(224),
                             self.position.getY() + self._calculate_point_pos_sin(224)),
                       Point(self.position.getX() + self._calculate_point_pos_cos(0),
                             self.position.getY() + self._calculate_point_pos_sin(0)))

    def _rotate(self, rotate_amount):
        self.rotation += rotate_amount
        self.triangle.undraw()
        self.triangle = self._create_triangle()
        self.triangle.draw(self.window)




