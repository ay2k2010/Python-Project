from libs.graphics import *

displayObjects = []

keyEventObjects = []
clickEventObjects = []
mouseEventObjects = []
tickEventObjects = []


class AdvancedShape(object):

    def display(self):
        raise NotImplementedError("display method not implemented")

    def key_event(self, key_event):
        raise NotImplementedError("key_event method not implemented")

    def click_event(self, click_event):
        raise NotImplementedError("click_event method not implemented")

    def mouse_event(self, mouse_event):
        raise NotImplementedError("mouse_event method not implemented")

    def tick_event(self):
        raise NotImplementedError("tick_event method not implemented")


def add_object(object, using_key_event=False, using_click_event=False, using_mouse_event=False, using_tick_event=False):
    """adds object to the appropriate event lists as well as adding it to the window"""

    displayObjects.append(object)

    if using_key_event:
        keyEventObjects.append(object)

    if using_click_event:
        clickEventObjects.append(object)

    if using_mouse_event:
        mouseEventObjects.append(object)

    if using_tick_event:
        tickEventObjects.append(object)


def loop(frames_per_second=30):
    """creates a window begins a loop that will update the window based on events and objects"""

    window = GraphWin()
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

        if window.mouseX is not None and window.mouseY is not None:
            mouse_event = Point(window.mouseX, window.mouseY)
            for object in mouseEventObjects:
                object.mouse_event(mouse_event)

        for object in tickEventObjects:
            object.tick_event()

        time.sleep(max(1 / frames_per_second - (time.time() - start_time), 0))
