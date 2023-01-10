#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hotdo
#
# Created:     17/06/2021
# Copyright:   (c) hotdo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    if is_even(n) == False:
        print ("This is an odd integer.")

    return n % 2 != 0