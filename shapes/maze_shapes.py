from core.advanced_shapes import *
from libs.graphics import *
from random import randint


class Maze(AdvancedShape):

    up = 1
    right = 2
    down = 3
    left = 4

    def __init__(self, size, scale, pos):
        self.size = size
        self.scale = scale
        self.center = pos
        self.maze = []
        self.window = None
        self.pos = Point(-1, -1)
        self.direction = self.up
        self.level = 1
        self.reversed_rotation = False
        self.direction_switched = 2

    def _generate_new_maze(self):
        self.maze = []
        self._create_start()
        while self.level < self.size:
            self._generate_part()
        self.draw()

    def _create_start(self):
        self.maze.append(Line(self.center, Point(self.center.getX(), self.center.getY() - self.scale)))
        self.maze.append(Line(Point(self.center.getX(), self.center.getY() - self.scale), Point(self.center.getX() + self.scale, self.center.getY() - self.scale)))
        self.maze.append(Line(Point(self.center.getX() + self.scale, self.center.getY() - self.scale), Point(self.center.getX() + self.scale, self.center.getY())))
        self.maze.append(Line(Point(self.center.getX() + self.scale, self.center.getY()), Point(self.center.getX() + self.scale, self.center.getY() + self.scale)))
        self.maze.append(Line(Point(self.center.getX() + self.scale, self.center.getY() + self.scale), Point(self.center.getX(), self.center.getY() + self.scale)))
        self.maze.append(Line(Point(self.center.getX(), self.center.getY() + self.scale), Point(self.center.getX() - self.scale, self.center.getY() + self.scale)))
        self.maze.append(Line(Point(self.center.getX() - self.scale, self.center.getY() + self.scale), Point(self.center.getX() - self.scale, self.center.getY())))
        self.maze.append(Line(Point(self.center.getX() - self.scale, self.center.getY()), Point(self.center.getX() - self.scale, self.center.getY() - self.scale)))

    def draw(self):
        for i in range(0, len(self.maze)):
            self.maze[i].draw(self.window)

    def _generate_part(self):

        if self.direction_switched > 0:
            self._possibly_switch_direction()

        if self.direction == self.up:
            if self.pos.getY() < -self.level:
                self._turn()
            else:
                self.maze.append(Line(self._pos_to_point(), self._pos_to_point(0, -1)))
                self.pos.y -= 1
        elif self.direction == self.down:
            if self.pos.getY() > self.level:
                self._turn()
                self.level += 1
            else:
                self.maze.append(Line(self._pos_to_point(), self._pos_to_point(0, 1)))
                self.pos.y += 1
        elif self.direction == self.left:
            if self.pos.getX() < -self.level:
                self._turn()
            else:
                self.maze.append(Line(self._pos_to_point(), self._pos_to_point(-1, 0)))
                self.pos.x -= 1
        elif self.direction == self.right:
            if self.pos.getX() > self.level:
                self._turn()
            else:
                self.maze.append(Line(self._pos_to_point(), self._pos_to_point(1, 0)))
                self.pos.x += 1

    def _possibly_switch_direction(self):
        if randint(0, self.level * 10) == 0:
            polarity = 1
            if self.reversed_rotation:
                polarity = -1
            if self.direction == self.up:
                self.maze.append(Line(self._pos_to_point(), self._pos_to_point(-1*polarity, 0)))
                self.pos.x -= 1*polarity
                self.direction = self.down
            elif self.direction == self.down:
                self.maze.append(Line(self._pos_to_point(), self._pos_to_point(1*polarity, 0)))
                self.pos.x += 1*polarity
                self.direction = self.up
            elif self.direction == self.left:
                self.maze.append(Line(self._pos_to_point(), self._pos_to_point(0, 1*polarity)))
                self.pos.y += 1*polarity
                self.direction = self.right
            elif self.direction == self.right:
                self.maze.append(Line(self._pos_to_point(), self._pos_to_point(0, -1*polarity)))
                self.pos.y -= 1*polarity
                self.direction = self.left
            self.level += 1
            self.reversed_rotation = not self.reversed_rotation
            self.direction_switched = 0

    def _turn(self):
        self.direction_switched += 1
        if self.reversed_rotation:
            self.direction -= 1
            if self.direction == 0:
                self.direction = 4
        else:
            self.direction = max(1, (self.direction + 1) % 5)

    def _pos_to_point(self, add_x=0, add_y=0):
        return Point(self.center.getX() + self.scale * (self.pos.getX() + add_x), self.center.getY() + self.scale * (self.pos.getY() + add_y))

    def click_event(self, click_event):
        pass

    def display(self, window):
        self.window = window
        self._generate_new_maze()

    def tick_event(self):
        pass

    def key_event(self, key_event):
        pass


class MazeSolver(AdvancedShape):

    def __init__(self, start_pos, scale):
        self.current_pos = Point(start_pos.getX() + scale / 2, start_pos.getY() - scale / 2)
        self.scale = scale
        self.circle = Circle(self.current_pos, 2)
        self.circle.setFill("green")
        self.circle.setOutline("green")
        self.window = None

    def display(self, window):
        self.circle.draw(window)
        self.window = window

    def key_event(self, key_event):
        if key_event == "w" or key_event == "Up":
            self._move(0, -1)
        elif key_event == "a" or key_event == "Left":
            self._move(-1, 0)
        elif key_event == "s" or key_event == "Down":
            self._move(0, +1)
        elif key_event == "d" or key_event == "Right":
            self._move(+1, 0)

    def _move(self, x, y):
        new_point = Point(self.current_pos.getX() + x * self.scale, self.current_pos.getY() + y * self.scale)
        line = Line(self.current_pos, new_point)
        line.setWidth(2)
        line.setOutline("green")
        self.circle.move(x * self.scale, y * self.scale)
        line.draw(self.window)
        self.current_pos = new_point
