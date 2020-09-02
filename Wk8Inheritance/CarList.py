from Car import Car


# a link class that contains a pointer to next and a reference to a car object
class Link:
    # init method that initializes the class variables
    def __init__(self, car):
        self.car = car
        self.next = None

    # setter to allow us to change the next value
    def setNext(self, next):
        self.next = next

    # getters to allow us to access the class variables
    def getNext(self):
        return self.next

    def getValue(self):
        return self.car


class CarList:
    def __init__(self):
        # car counter instead of interating through the list every time.
        self.counter = 0
        self.head = None

    # input is make, color, year. Creates a new car, creates a new link that points to that car
    # and adds it to the head of the list
    def addCar(self, make, color, year):
        # temp holds our link
        temp = Link(Car(make, color, year))
        self.counter += 1
        # testing head
        if self.head == None:
            # changes head to the link holder
            self.head = temp
            return
        # handle if list is not empty
        temp.setNext(self.head)
        self.head = temp

    # input is make, color, year. Creates a temporary car with those inputs. Uses the
    # overloaded equality operator to check the list to see if such a car exists. Returns true if found, false
    def findCar(self, make, color, year):
        current = self.head
        tempCar = Car(make, color, year)

        while current != None:
            if current.getValue() == tempCar:
                return True
            current = current.getNext()
        return False

    # if list is empty, returns none. Otherwise returns the car at the head of the list
    # and removes it from the list
    def removeHead(self):
        if self.head == None:
            return None
        self.counter -= 1
        temp = self.head
        self.head = self.head.getNext()
        # little car is a variable in the link class
        return temp.getValue()

    # Overloaded str() method that uses the car str() method to create a string of all the cars in the list.
    # The cars should be listed one per line.
    def __str__(self):
        current = self.head
        cars = ""
        while current != None:
            # invoking our overloaded string method in the Car class
            # cars = cars + str(current.car) + "\n"
            print(current.car)
            current = current.getNext()
        # a string of all cars
        return cars

        # Overloaded len() method that returns the number of cars in the list

    def __len__(self):
        return self.counter
