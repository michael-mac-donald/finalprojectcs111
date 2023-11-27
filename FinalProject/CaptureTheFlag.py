# Michael MacDonald and Joey Sullivan
# Final Project - Capture The Flag
# Various
# Capture The Flag Game

from sac_graphics import *
import time

def main():
    w, h = 1200, 800
    win = GraphWin("Capture the Flag", w, h)
    win.setBackground(color_rgb(220,220,220))

    playbutton = Rectangle(Point(w/2 + 100, 150), Point(w/2 - 100, 225))
    playbutton.setFill(color_rgb(145, 153, 255))
    playbutton.setOutline(color_rgb(0, 0, 255))
    playbutton.setWidth(4)

    playtext = Text(playbutton.getCenter(),"Play")
    playtext.setStyle("bold")
    playtext.setFace("courier")
    playtext.setSize(24)

    infobutton = Rectangle(Point(w / 2 + 100, 300), Point(w / 2 - 100, 375))
    infobutton.setFill(color_rgb(255, 153, 142))
    infobutton.setOutline(color_rgb(255, 0, 0))
    infobutton.setWidth(4)

    infotext = Text(infobutton.getCenter(), "How to Play")
    infotext.setStyle("bold")
    infotext.setFace("courier")
    infotext.setSize(24)

    creditsbutton = Rectangle(Point(w / 2 + 100, 450), Point(w / 2 - 100, 525))
    creditsbutton.setFill(color_rgb(145, 153, 255))
    creditsbutton.setOutline(color_rgb(0, 0, 255))
    creditsbutton.setWidth(4)

    creditstext = Text(creditsbutton.getCenter(), "Credits")
    creditstext.setStyle("bold")
    creditstext.setFace("courier")
    creditstext.setSize(24)

    for i in range(1, 50):
        file = "assets/title/frame-" + str(i) + ".png"
        title = Image((Point(w / 2, 50)), file)
        title.draw(win)

    playbutton.draw(win)
    time.sleep(.2)
    infobutton.draw(win)
    time.sleep(.2)
    creditsbutton.draw(win)
    time.sleep(.2)
    playtext.draw(win)
    time.sleep(.2)
    infotext.draw(win)
    time.sleep(.2)
    creditstext.draw(win)

    print(win.getMouse())


if __name__ == "__main__":
    main()