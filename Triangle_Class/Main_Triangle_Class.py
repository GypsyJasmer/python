from Triangle import Triangle


def main():
    first = Triangle()

    print("\nTest if default is properly created\n")
    print("Default should be 3, 4 5 triangle and both scalene and right")
    print(" for default a is " + str(first.getA()) + " b is " + str(first.getB()) + " c is " + str(first.getC()))
    print("First is: ", end="")
    if first.isEquilateral():
        print(" equilateral ", end="")
    if first.isIsosceles():
        print(" isosceles ", end="")
    if first.isScalene():
        print(" scalene ", end="")
    if first.isRight():
        print(" right ", end="")

    print("\n\nTest setter methods\n")
    first.setA(2)
    first.setB(2)
    first.setC(3)
    print("Modified first should be 2, 2, 3 triangle and isoosceles")
    print(" for modified a is " + str(first.getA()) + " b is " + str(first.getB()) + " c is " + str(first.getC()))
    print("First now is: ", end="")
    if first.isEquilateral():
        print(" equilateral ", end="")
    if first.isIsosceles():
        print(" isosceles ", end="")
    if first.isScalene():
        print(" scalene ", end="")
    if first.isRight():
        print(" right ", end="")

    print("\n\nTest overloaded constructor\n")
    second = Triangle(4, 4, 4)
    print("Second should be 4, 4, 4, triangle and should be both equilateral and isosceles")
    print(" for second a is " + str(second.getA()) + " b is " + str(second.getB()) + " c is " + str(second.getC()))
    print("Second is: ", end="")
    if second.isEquilateral():
        print(" equilateral ", end="")
    if second.isIsosceles():
        print(" isosceles ", end="")
    if second.isScalene():
        print(" scalene ", end="")
    if second.isRight():
        print(" right ", end="")


if __name__ == '__main__':
    main()