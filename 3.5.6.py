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
window.bgcolor("skyblue")

joshua = turtle.Turtle()

def drunkturtle(animal):
    joshua.color("purple")
    joshua.pendown()
for turn in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    joshua.left(turn)
    joshua.forward(100)
