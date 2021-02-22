"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
state = False
vy = 0

ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)

window = GWindow(800, 500, title='bouncing_ball.py')

count = 0

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global state, vy, count
    window.add(ball)

    while True:
        if state is True and count < 3:
            vy += GRAVITY
            pause(DELAY)
            if ball.y >= 500:
                vy = -REDUCE * vy

            ball.move(VX, vy)
            print(ball.x, ball.y)

            if ball.x >= window.width:

                ball.x = START_X
                ball.y = START_Y
                state = False
                count += 1

        pause(DELAY)
        onmouseclicked(trigger)

    print("ended")
    # if clicked == 3:
    #     onmouseclicked()

def trigger(event):
    # if objects in window = 0
    global state, count
    state = True

# def do_nothing(nothing):
#     nothing

if __name__ == "__main__":
    main()
