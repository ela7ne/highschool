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
window.bgcolor("thistle")

alex = turtle.Turtle()
alex.pensize(3)
alex.shape("turtle")
alex.color("blue")

for i in range(12):
     alex.penup()
     alex.fd(80)
     alex.pendown()
     alex.fd(10)
     alex.penup()
     alex.fd(30)
     alex.stamp()
     alex.backward(120)
     alex.rt(30)

alex.stamp()

window.mainloop()