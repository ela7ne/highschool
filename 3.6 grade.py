#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hotdo
#
# Created:     10/02/2022
# Copyright:   (c) hotdo 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def get_grade(mark):
    if mark >= 75:
            return "first"
    else:
        if mark >= 70:
                return "upper second"
        else:
            if mark >= 60:
                    return "second"
            else:
                if mark >= 50:
                        return "third"
                else:
                        if mark >= 45:
                            return "f1 supp"
                        else:
                            if mark > 40:
                                return "f2"
                            else:
                                return "f3"

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for x in xs:
    print("mark: " + str(x) + " grade: " + get_grade(x))
