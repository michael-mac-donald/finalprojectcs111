# Michael MacDonald and Joey Sullivan
# Final Project - Capture The Flag
# Game
# Game Classes for Capture The Flag Game

from sac_graphics import *
import time

class Game:

    def __init__(self, win, w, h):
        self.win = win
        self.blueside = Rectangle(Point(0, h), Point(w / 2, 0))
        self.blueside.setFill(color_rgb(145, 153, 255))

        self.redside = Rectangle(Point(w / 2, h), Point(w, 0))
        self.redside.setFill(color_rgb(255, 153, 142))

        self.bplayer = Circle(Point(w / 4, h / 2), 22)
        self.bplayer.setFill("blue")
        self.bplayer.setOutline(color_rgb(0, 13, 128))
        self.bplayer.setWidth(4)

        self.rplayer = Circle(Point(w * 3 / 4, h / 2), 22)
        self.rplayer.setFill("red")
        self.rplayer.setOutline(color_rgb(128, 13, 0))
        self.rplayer.setWidth(4)

        self.bsafe = Rectangle(Point(0, h), Point(w / 15, 0))
        self.bsafe.setFill(color_rgb(255, 198, 191))
        self.bsafe.setWidth(1)

        self.rsafe = Rectangle(Point(w, h), Point(w * 14 / 15, 0))
        self.rsafe.setFill(color_rgb(191, 198, 255))
        self.rsafe.setWidth(1)

        self.rflag = Image(Point(1200, 400), "assets/flags/rflag.png")
        self.bflag = Image(Point(200, 400), "assets/flags/bflag.png")

        self.rsafezonetext = Image(Point(50, 415), "assets/rsafezone.png")

        self.bsafezonetext = Image(Point(1350, 385), "assets/bsafezone.png")

        self.target_point = None
        self.collision_circle = None

    def drawgame(self):

        self.blueside.draw(self.win)
        self.redside.draw(self.win)
        self.bsafe.draw(self.win)
        self.rsafe.draw(self.win)
        self.rflag.draw(self.win)
        self.bflag.draw(self.win)
        self.rsafezonetext.draw(self.win)
        self.bsafezonetext.draw(self.win)
        self.bplayer.draw(self.win)
        self.rplayer.draw(self.win)

    def undrawgame(self):

        self.blueside.undraw()
        self.redside.undraw()
        self.bplayer.undraw()
        self.rplayer.undraw()
        self.bsafe.undraw()
        self.rsafe.undraw()
        self.rflag.undraw()
        self.bflag.undraw()
        self.rsafezonetext.undraw()
        self.bsafezonetext.undraw()

    def make_collision_circle(self, center):
        if self.collision_circle:
            self.collision_circle.undraw()
        self.collision_circle = Circle(center, 5)


    def move(self):
        flag = True
        while flag:
            rdx, rdy, bdx, bdy = 0, 0, 0, 0
            key = self.win.checkKey()
            bplayer_x, bplayer_y = self.bplayer.getCenter().getX(), self.bplayer.getCenter().getY()
            rplayer_x, rplayer_y = self.rplayer.getCenter().getX(), self.rplayer.getCenter().getY()

            if key == 'w':
                bdy = -10
            elif key == 's':
                bdy = 10
            elif key == 'a':
                bdx = -10
            elif key == 'd':
                bdx = 10

            mouse_point = self.win.checkMouse()

            if mouse_point:
                self.target_point = mouse_point
                self.make_collision_circle(self.target_point)

            if self.target_point:
                dx = self.target_point.getX() - self.rplayer.getCenter().getX()
                dy = self.target_point.getY() - self.rplayer.getCenter().getY()

                distance = ((dx ** 2) + (dy ** 2)) ** 0.5

                min_distance = self.rplayer.getRadius() + self.collision_circle.getRadius()

                if distance > min_distance:

                    dx /= distance
                    dy /= distance

                    self.rplayer.move(dx * 10, dy * 10)
                else:
                    self.target_point = None

            new_bplayer_x, new_bplayer_y = bplayer_x + bdx, bplayer_y + bdy
            new_rplayer_x, new_rplayer_y = rplayer_x + rdx, rplayer_y + rdy

            if 0 <= new_bplayer_x <= self.win.getWidth() and 0 <= new_bplayer_y <= self.win.getHeight():
                self.bplayer.move(bdx, bdy)

            if 0 <= new_rplayer_x <= self.win.getWidth() and 0 <= new_rplayer_y <= self.win.getHeight():
                self.rplayer.move(rdx, rdy)
            time.sleep(.05)
