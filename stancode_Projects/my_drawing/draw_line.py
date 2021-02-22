"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
window = GWindow()

SIZE = 10
click_sum = 0
first_x = 0
first_y = 0

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)

def draw(mouse):
    global first_x, first_y, click_sum

    if click_sum % 2 == 0:
        oval = GOval(SIZE, SIZE)
        window.add(oval, mouse.x - SIZE/2, mouse.y - SIZE/2)
        first_x = mouse.x
        first_y = mouse.y

    else:
        hole = window.get_object_at(first_x, first_y)

        window.remove(hole)
        line = GLine(mouse.x, mouse.y, first_x, first_y)
        window.add(line)

    click_sum += 1


if __name__ == "__main__":
    main()
