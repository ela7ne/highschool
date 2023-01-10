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
wn = turtle.Screen()

wn.bgcolor("lightgreen")
wn.title("Two spirals")


def square_spiral(ttl, trn, fwd):
    ttl.color("blue")
    ttl.pensize(1.5)
    ttl.speed(10)

    ttl.penup()
    ttl.forward(fwd)

    ttl.pendown()
    for i in range(0, 100):
        ttl.forward(i * 2)
        ttl.right(trn)

tess = turtle.Turtle()
square_spiral(tess, 90, -150)

alex = turtle.Turtle()
square_spiral(alex, 89, 150)

wn.mainloop()
