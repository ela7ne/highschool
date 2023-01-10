#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hotdo
#
# Created:     03/04/2022
# Copyright:   (c) hotdo 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def slope(x1, y1, x2, y2):
    return (y2 - y1)/(x2 - x1)

def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    return float(y1 - m*x1)
