#-------------------------------------------------------------------------------
# Name:        module1
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

mark = int(input("what is your mark"))

def grade(mark):
    if mark >= 75:
        return "first"
    elif  mark >= 70-75:
            return "upper second"
    elif mark >= 60-70:
                return "second"
    elif mark >= 50-60:
                    return "third"
    elif mark >= 45-50:
                        return "f1 supp"
    elif mark >= 40-45:
                            return "f2"
    elif mark <= 40:
                                return "f3"
    else:
        return None

print(mark)