from Car import Car
from CarList import CarList


def main():
    print("This tests car class\n")
    car1 = Car()
    car2 = Car("Pinto", "Purple", 1968);
    truck1 = Car("Toyota", "Blue", 2010);
    truck2 = Car("Jeep", "Green", 2008);

    print("Testing default initialization.\n Should be: Black 1910 Ford \n is: ", end="")
    print(str(car1.getColor()) + " " + str(car1.getYear()) + " " + str(car1.getMake()), end="\n\n")

    print("Testing overloaded initialization.\n Should be: Purple 1968 Pinto \n is: ", end="")
    print(str(car2.getColor()) + " " + str(car2.getYear()) + " " + str(car2.getMake()), end="\n\n")

    print("Testing setters")
    print("Should start as a Blue 2010 Toyota \n is:", end="")
    print(str(truck1), end="\n\n")
    print("Should have changed to green 2008 Jeep\n is:", end="")
    truck1.setColor("Green")
    truck1.setYear(2008)
    truck1.setMake("Jeep")
    print(str(truck1), end="\n\n")

    print("Testing string operator, next two lines should match")
    print(str(car2.getColor()) + " " + str(car2.getYear()) + " " + str(car2.getMake()))
    print(str(car2))

    print("\nTesting equality operator")
    print("First: is " + str(car1) + " == " + str(truck1), end="? ")
    if car1 == truck1:
        print("yes")
    else:
        print("no")
    print("First: is " + str(truck1) + " == " + str(truck2), end="? ")
    if truck1 == truck2:
        print("yes")
    else:
        print("no")

    print("\nDone with testing Car class \n")

    print("\nTesting CarList class")

    theList = CarList()

    print("\nTesting adding items and displaying them")
    theList.addCar("Taxi", "Yellow", 1992);
    theList.addCar("Ford", "White", 2017);
    theList.addCar("Honda", "Blue", 2010);
    theList.addCar("Chevy", "Green", 2012);

    print("\nDisplaying the list, it should be: ")
    print("Green 2012 Chevy\nBlue 2010 Honda\nWhite 2017 Ford\nYellow 1992 Taxi \n")
    print("It actually is: ")
    print(str(theList))

    print("\nTesting find ")
    print("Blue 2018 Chevy should not be there and ", end="")
    if theList.findCar("Chevy", "Blue", 2018):
        print("it is")
    else:
        print("it is not")
    print("White 2017 Ford should be there and ", end="")
    if theList.findCar("Ford", "White", 2017):
        print("it is")
    else:
        print("it is not")

    print("\nTesting length, list should be 4 and is " + str(len(theList)))

    print("\nTesting remove head by removing and displaying each car until None is reached")
    tempCar = theList.removeHead()
    while tempCar:
        print(str(tempCar))
        tempCar = theList.removeHead()

    print("\nNow testing find on empty List ")
    print("White 2017 Ford should not be there, and ", end="")
    if theList.findCar("Ford", "White", 2017):
        print("it is")
    else:
        print("it is not")

    print("\nDone with testing CarList class")


if __name__ == '__main__':
    main()

