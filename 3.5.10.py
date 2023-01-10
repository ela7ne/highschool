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
window.bgcolor("thistle")

mark = turtle.Turtle()

for i in range(5):
    mark.fd(100)
    mark.right(144)

window.mainloop()