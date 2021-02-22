"""
File: 
Name:
----------------------
TODO:
"""



from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
    window = GWindow(width=800, height=800)

    labelrect = GRect(450, 60, x= 25, y = 5)
    labelrect.filled = True
    labelrect.color = "pink"
    labelrect.fill_color = "pink"
    window.add(labelrect)

    label = GLabel("Kirby, by Larry, 2020/12", 30, 55)
    label.font = "SansSerif-18"
    label.font = "-40"
    label.color = "white"
    window.add(label)

    l_hand = GOval(200, 200, x = 30, y = 330)
    l_hand.filled = True
    l_hand.fill_color = "pink"
    window.add(l_hand)

    r_hand = GOval(200, 200, x=570, y=330)
    r_hand.filled = True
    r_hand.fill_color = "pink"
    window.add(r_hand)

    l_foot = GOval(250, 300, x=120, y=500)
    l_foot.filled = True
    l_foot.fill_color = "magenta"
    window.add(l_foot)

    r_foot = GOval(250, 300, x=430, y=500)
    r_foot.filled = True
    r_foot.fill_color = "magenta"
    window.add(r_foot)


    K_body = GOval(600, 600, x = 100, y = 100)
    K_body.filled = True
    K_body.fill_color = "pink"
    window.add(K_body)

    l_eyeblue = GOval(60, 90, x=285, y=220)
    l_eyeblue.filled = True
    l_eyeblue.fill_color = "blue"
    window.add(l_eyeblue)

    r_eyeblue = GOval(60, 90, x=455, y=220)
    r_eyeblue.filled = True
    r_eyeblue.fill_color = "blue"
    window.add(r_eyeblue)

    l_eyeblack = GOval(50, 70, x=290, y=220)
    l_eyeblack.filled = True
    l_eyeblack.color = "black"
    l_eyeblack.fill_color = "black"
    window.add(l_eyeblack)

    r_eyeblack = GOval(50, 70, x=460, y=220)
    r_eyeblack.filled = True
    r_eyeblack.color = "black"
    r_eyeblack.fill_color = "black"
    window.add(r_eyeblack)

    # x = 315
    l_eye = GOval(30, 40, x=300, y=220)
    l_eye.filled = True
    l_eye.color = "white"
    l_eye.fill_color = "white"
    window.add(l_eye)

    # x = 485
    r_eye = GOval(30, 40, x=470, y=220)
    r_eye.filled = True
    r_eye.color = "white"
    r_eye.fill_color = "white"
    window.add(r_eye)

    mouth = GArc(200, 100, -9, -120, 315, 320)
    window.add(mouth)

    # x = 245
    l_flush = GOval(50, 30, x=220, y=320)
    l_flush.filled = True
    l_flush.color = "pink"
    l_flush.fill_color = "magenta"
    window.add(l_flush)

    # x =  555
    r_flush = GOval(50, 30, x=530, y=320)
    r_flush.filled = True
    r_flush.color = "pink"
    r_flush.fill_color = "magenta"
    window.add(r_flush)

    window.add(arc)

if __name__ == '__main__':
    main()
