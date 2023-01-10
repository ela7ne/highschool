#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      hotdo
#
# Created:     10/06/2021
# Copyright:   (c) hotdo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("hotpink")

def draw_square(t,size):
    for i in range(4):
        tess.fd(size)
        tess.lt(90)

size = 20
for j in range(5):
   tess.pensize(3)
   draw_square(tess,size)
   size = size + 20
   tess.penup()
   tess.goto(tess.pos() + (-10, -10))
   tess.pendown()

window.mainloop()