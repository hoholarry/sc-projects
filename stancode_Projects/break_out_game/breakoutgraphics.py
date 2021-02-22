"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # numberx of rows of bricks.
BRICK_COLS = 10        # numberx of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        self.game_started = False

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window_height = window_height
        self.window_width = window_width

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle,window_width/2, window_height - paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, window_width/2, window_height/2)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0

        #draw brick
        self.drawbricks()

        # Initialize our mouse listeners.
        onmousemoved(self.movepaddle)
        onmouseclicked(self.startgame)

        # score
        self.score = 0
        self.scoreboard = GLabel("Score:" + str(self.score))
        self.scoreboard.font = '-30'


    def movepaddle(self, mouse): # 移動板子
        if mouse.x >= self.window_width - self.paddle.width/2:
            self.paddle.x = self.window_width - self.paddle.width
        elif mouse.x <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - PADDLE_WIDTH / 2


    def startgame(self, event): # 開始遊戲
        if self.game_started is False:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if (random.random() > 0.5):
                self.__dx = -self.__dx
            self.game_started = True

    def drawbricks(self): # 產生方塊
        numberx = 0
        numbery = 0

        for y in range(BRICK_COLS):
            for x in range(BRICK_ROWS):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                if numbery < 2:
                    brick.filled = True
                    brick.fill_color = "red"
                if numbery < 4 and numbery >= 2:
                    brick.filled = True
                    brick.fill_color = "orange"
                if numbery < 6 and numbery >= 4:
                    brick.filled = True
                    brick.fill_color = "yellow"
                if numbery < 8 and numbery >= 6:
                    brick.filled = True
                    brick.fill_color = "green"
                if numbery < 10 and numbery >= 8:
                    brick.filled = True
                    brick.fill_color = "blue"

                self.window.add(brick, (BRICK_WIDTH + BRICK_SPACING) * numberx, (BRICK_HEIGHT + BRICK_SPACING) * numbery)
                numberx += 1
                if numberx > 9:
                    numberx = 0
            numbery += 1

    def boundary(self): # 邊框反彈
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = - self.__dx
        if self.ball.y <= 0:
            self.__dy = - self.__dy

    def getx(self): # 傳 x 的速度給動畫
        return self.__dx

    def gety(self): # 傳 y 的速度給動畫
        return self.__dy

    def reset_ball(self): # 重設球的位置
        self.set_ball_position()
        while self.ball_fall_down():
            self.set_ball_position()
        self.__dx = 0
        self.__dy = 0

    def set_ball_position(self): # 重生位置
        self.ball.x = self.window_width/2
        self.ball.y = self.window_height/2

    def ball_fall_down(self): # 球掉落
        if self.ball.y > self.window_height:
            print("dead")
            self.game_started = False
            return True

    def collision(self): # 偵測撞擊
        maybe_coll_tr = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_coll_tl = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y)
        maybe_coll_br = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS)
        maybe_coll_bl = self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS)

        if maybe_coll_tr is self.scoreboard or maybe_coll_tl is self.scoreboard or maybe_coll_br is self.scoreboard or maybe_coll_bl is self.scoreboard:
            print('in if')
            pass
        elif maybe_coll_tr is not None or maybe_coll_tl is not None or maybe_coll_br is not None or maybe_coll_bl is not None:
            print('hit')
            if self.ball.y < self.window_height/2:
                self.__dy = - self.__dy
                self.window.remove(maybe_coll_bl)
                self.window.remove(maybe_coll_br)
                self.window.remove(maybe_coll_tr)
                self.window.remove(maybe_coll_tl)
                self.score += 1
                self.scoreboard.text = "Score: " + str(self.score)
            elif self.ball.y > self.window_height/2:
                print('hit lower half')
                if self.__dy > 0:
                    self.__dy = - self.__dy

    def you_win(self): # 勝利
        if self.score == 40:
            self.you_win_tag = GLabel("YOU WIN")
            self.window.add(self.you_win_tag, 120, self.window_height/2)
            self.you_win_tag.font = '-40'
            return True

    def game_over(self): # 死掉三次
        self.game_over_tag = GLabel("GAME OVER")
        self.window.add(self.game_over_tag, 120, self.window_height/2)
        self.game_over_tag.font = '-40'