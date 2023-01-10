#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      hotdo
#
# Created:     07/02/2022
# Copyright:   (c) hotdo 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))


def check_right_angle(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a) :
        return False
    else:
        return True

if check_right_angle(a, b, c):
    print("valid")
else:
    print("invalid")