# ==============================================================================================================
# Python file that adds a simple was for objects to be drawn on screen using graphics.py library
# It adds an easy way na object to rendered and to respond to events with extra features like stable frame rate
# ==============================================================================================================
# AdvancedShape
# - - - - - - -
# all shape objects that want to be a part of the loop and event system must extend/implement this class
# provides simple methods that will be called from any object that subscribes to that event
# --------------------------------------------------------------------------------------------------------------
# add_object
# - - - - -
# any shape object must be passed trough this function prior to activating the loop
# add_object's first parameter is the object and is required
# next parameters are boolean which allow the object to subscribe to different events (default is False)
# --------------------------------------------------------------------------------------------------------------
# loop
# - -
# the loop function starts the whole system by creating the graphics window
# the loop then cycles(or loops) x(first parameter) amounts per second (default 30)
# the loop check if an event occurred and notifies the objects subscribed to it.
# loop will eventually crash when window is exited
# ==============================================================================================================
from libs.graphics import *

displayObjects = []

keyEventObjects = []
clickEventObjects = []
tickEventObjects = []


class AdvancedShape(object):
    """abstract class for all shape object displayed in window allowing for event updates"""
    def display(self, window):
        raise NotImplementedError("display method not implemented")

    def key_event(self, key_event):
        raise NotImplementedError("key_event method not implemented")

    def click_event(self, click_event):
        raise NotImplementedError("click_event method not implemented")

    def tick_event(self):
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
