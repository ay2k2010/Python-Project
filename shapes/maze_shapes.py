from core.advanced_shapes import *
from libs.graphics import *


class Maze(AdvancedShape):

    def __init__(self, size, scale, pos):
        self.size = size
        self.scale = scale
        self.center = pos
        self.maze = []
        self.window = None

    def generate_new_maze(self):
        self.maze = []
        self.create_start()
        self.draw()

    def create_start(self):
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

    def click_event(self, click_event):
        pass

    def display(self, window):
        self.window = window
        self.generate_new_maze()

    def tick_event(self):
        pass

    def key_event(self, key_event):
        pass


class MazeSolver(AdvancedShape):

    def __init__(self, start_pos, scale):
        self.current_pos = Point(start_pos.getX() - scale / 2, start_pos.getY() - scale / 2)
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
        line.draw(self.window)
        self.current_pos = new_point
        self.circle.move(x * self.scale, y * self.scale)
