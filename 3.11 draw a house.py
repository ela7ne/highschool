#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hotdo
#
# Created:     10/02/2022
# Copyright:   (c) hotdo 2022
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
tess.pensize(4)


def house(turtle, moves):
    for x in moves:
        turtle.left(x[0])
        turtle.fd(x[1])


o = 100
f = 0.5
moves = [(180, o), (-135, o*2**f), (135, o), (135, o*2**f), (135, o), (45, o*.5**f), (90, o*.5**f), (45, o)]

house(tess, moves)

window.mainloop()