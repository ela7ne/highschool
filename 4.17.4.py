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

def day_name(number):
    if number == 0:
        return ('Sunday')
    elif number == 1:
        return ('Monday')
    elif number == 2:
        return ('Tuesday')
    elif number == 3:
        return ('Wednesday')
    elif number == 4:
        return ('Thursday')
    elif number == 5:
        return ('Friday')
    elif number == 6:
        return ('Saturday')
    else:
        return None


def day_num(day_name):
    if day_name == 'Sunday':
        return (0)
    elif day_name == 'Monday':
        return (1)
    elif day_name == 'Tuesday':
        return (2)
    elif day_name == 'Wednesday':
        return (3)
    elif day_name == 'Thursday':
        return (4)
    elif day_name == 'Friday':
        return (5)
    elif day_name == 'Saturday':
        return (6)
    else:
        return None


def day_add(today, stay):
    today = day_num(today)
    day_back = (stay % 7) + today
    result = day_name(day_back)
    return (result)