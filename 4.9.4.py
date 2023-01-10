#-------------------------------------------------------------------------------
# Name:        module1
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

def draw_poly(t, n, sz):

    for i in range(n):
        t.forward(sz)
        t.left(360 / n)

import turtle

joshua = turtle.Turtle()
joshua.color("blue")
joshua.pensize(2)

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("pretty pattern")

for i in range(0, 20):
    draw_poly(joshua, 4, 100)
    joshua.right(18)

window.mainloop()