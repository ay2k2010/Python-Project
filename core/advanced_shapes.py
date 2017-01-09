# ==============================================================================================================
#                           ▀▀█▀▀ ▒█░▒█ ▒█▀▀▀ 　 ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀
#                           ░▒█░░ ▒█▀▀█ ▒█▀▀▀ 　 ▒█░░░ ▒█░░▒█ ▒█▄▄▀ ▒█▀▀▀
#                           ░▒█░░ ▒█░▒█ ▒█▄▄▄ 　 ▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▄
# ==============================================================================================================
# Python file that adds a simple core for objects to be drawn on screen using the graphics.py library
# It adds an easy way for an object to rendered and to respond to events along with extra features
# ==============================================================================================================
# AdvancedShape
# - - - - - - -
# all shape objects that want to be a part of the loop and event system must extend/implement this class
# provides simple methods that will be called from any object that subscribes to that event
# examples ate in the shapes.test_shapes.py file
# --------------------------------------------------------------------------------------------------------------
# add_object
# - - - - -
# any shape object must be passed trough this function prior to activating the loop
# add_object's first parameter is the object and is required
# next parameters are boolean which allow the object to subscribe to different events (default is False)
# examples ate in the core.__init__.py file
# --------------------------------------------------------------------------------------------------------------
# loop
# - -
# the loop function starts the whole system by creating the graphics window
# the loop then cycles(or loops) x amounts per second
# x is determined by first parameter ex. 'loop(20)' or if no parameters are given the default is 30
# the loop checks if an event occurred and notifies the objects subscribed to that event through add_object
# loop will crash when window is exited (known bug)
# ==============================================================================================================
from libs.graphics import *

displayObjects = []

keyEventObjects = []
clickEventObjects = []
tickEventObjects = []


class AdvancedShape(object):
    """abstract class for all shape object displayed in window allowing for event updates"""
    def display(self, window):
        """called once at the beginning of the program"""
        raise NotImplementedError("display method not implemented")

    def key_event(self, key_event):
        """called anytime a key is pressed (only one key detected at a time)"""
        raise NotImplementedError("key_event method not implemented")

    def click_event(self, click_event):
        """called every time the mouse left clicks"""
        raise NotImplementedError("click_event method not implemented")

    def tick_event(self):
        """called at the end of every cycle or loop"""
        raise NotImplementedError("tick_event method not implemented")


def add_object(object, using_key_event=False, using_click_event=False, using_tick_event=False):
    """adds object to the appropriate event lists as well as adding it to the window"""

    displayObjects.append(object)

    if using_key_event:
        keyEventObjects.append(object)

    if using_click_event:
        clickEventObjects.append(object)

    if using_tick_event:
        tickEventObjects.append(object)


def loop(frames_per_second=30):
    """creates a window begins a loop that will update the window based on events and objects"""

    window = GraphWin("Test", 640, 480)
    is_running = True

    for object in displayObjects:
        object.display(window)

    while is_running:
        start_time = time.time()

        key_event = window.checkKey()
        click_event = window.checkMouse()

        if key_event != "":
            for object in keyEventObjects:
                object.key_event(key_event)

        if click_event is not None:
            for object in clickEventObjects:
                object.click_event(click_event)

        for object in tickEventObjects:
            object.tick_event()

        time.sleep(max(1 / frames_per_second - (time.time() - start_time), 0))
