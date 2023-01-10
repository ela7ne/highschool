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

import turtle

window = turtle.Screen()
window.bgcolor("skyblue")

triangle = turtle.Turtle()

for i in range (3):
    triangle.forward(120)
    triangle.lt(120)


square = turtle.Turtle()
square.up()
square.forward(100)
square.down()

for i in range (4):
    square.forward(50)
    square.left(90)
hex =turtle.Turtle()
hex.up()
hex.forward(-70)
hex.down()

for i in range (6):
    hex.forward(30)
    hex.left(60)
oct =turtle.Turtle()
oct.up()
oct.forward(-170)
oct.down()

for i in range (8):
    oct.forward(25)
    oct.left(45)
