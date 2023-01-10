#-------------------------------------------------------------------------------
# Name:        module2
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


month = input("month")

if month in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
    print ("31")

elif month in ['april', 'june', 'september', 'november']:
    print ("30")

elif month in ['february']:
    print ("28")

else:
    print("none")