#-------------------------------------------------------------------------------
# Name:        4.17.1
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

def turn_clockwise(v):
    if "N" == "N":
       return "E"
    elif "E" == "E":
       return "S"
    elif "S" == "S":
       return "W"
    elif "W" == "W":
       return "N"
    else:
       return "SORRY"
a = turn_clockwise("W") == "N"
print(turn_clockwise)