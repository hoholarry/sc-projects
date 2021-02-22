"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES # 生命

    graphics.window.add(graphics.scoreboard, 0, graphics.window_height) # 計分板

    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.ball_fall_down():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                graphics.game_over()
                break
        if graphics.you_win():
            break
        vx = graphics.getx()
        vy = graphics.gety()
        graphics.ball.move(vx, vy)
        graphics.boundary()
        graphics.collision()


if __name__ == '__main__':
    main()
