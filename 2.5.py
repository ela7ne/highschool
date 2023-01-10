#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hotdo
#
# Created:     01/02/2022
# Copyright:   (c) hotdo 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


P = 35000
n = 1 #compounded anually, so once a year
r = 0.4

t = int(input("how many years would you like your investment to grow"))


#compound interest formula simplified
x = 1  + r / n
A = P * x ** (n * t)


text = "you will have ${:,} after {} years."
print(text.format(round(A,2), t))