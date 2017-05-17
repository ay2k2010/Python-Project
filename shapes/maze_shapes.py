from core.advanced_shapes import *
from libs.graphics import *


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
        self.horizontal_lines = [[0 for x in range(self.size-1)] for y in range(self.size)]
        self.vertical_lines = [[0 for x in range(self.size)] for y in range(self.size-1)]
        self.window = None
        self.pos = Point(int(self.size/2), int(self.size/2))
        self.direction = self.up
        self.level = 2

    def _generate_new_maze(self):
        self.maze = []
        self._create_start()
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
        if self.direction == self.up:
            if self.pos.getY() - self.size/2 > self.level:
                self._turn()
            else:
                self.vertical_lines[self.pos.getX()][self.pos.getY() + 1] = 1
        elif self.direction == self.down:
            if self.pos.getY() + self.size / 2 > self.level:
                self._turn()
            else:
                self.vertical_lines[self.pos.getX()][self.pos.getY() - 1] = 1
        elif self.direction == self.left:
            if self.pos.getX() - self.size / 2 > self.level:
                self._turn()
            else:
                self.horizontal_lines[self.pos.getX() + 1][self.pos.getY() ] = 1
        elif self.direction == self.right:
            if self.pos.getX() + self.size / 2 > self.level:
                self._turn()
            else:
                self.horizontal_lines[self.pos.getX() - 1][self.pos.getY()] = 1

    def _turn(self):
        pass

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
