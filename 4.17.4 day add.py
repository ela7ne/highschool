#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      hotdo
#
# Created:     02/04/2022
# Copyright:   (c) hotdo 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


def day_name(num):
    days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday",
            "saturday")
    try:
        #i wanted to try "try and except" as its something new
        return days[num]
    except:
        return None

def day_num(day):
    days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday",
            "saturday")
    try:
        return days.index(day)
    except:
        return None


def day_add(day, num):
    number = (day_num(day) + num) % 7
    return day_name(number)