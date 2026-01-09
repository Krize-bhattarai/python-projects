import turtle as tl
import colorsys as cs

tl.setpos(0, 80)
tl.speed(0)
tl.bgcolor("black")
tl.pensize(2)

h = 0.71

for i in range(150):
    r, g, b = cs.hsv_to_rgb(h, 1, 1)
    tl.color(r, g, b)
    h += 0.004

    tl.circle(139, 90)
    tl.left(90)
    tl.left(20)
    tl.circle(139, 90)
    tl.left(18)

tl.hideturtle()
tl.done()
# Python Codes
