class Car:
    def __init__(self, make="Ford", color="Black", year=1910):
        self.make = make
        self.color = color
        self.year = year

    # setters and getters for all three variables
    def setMake(self, make):
        self.make = make

    def setColor(self, color):
        self.color = color

    def setYear(self, year):
        self.year = year

    def getMake(self):
        return self.make

    def getColor(self):
        return self.color

    def getYear(self):
        return self.year

    # Overloaded equality operator that matches all three variables, return true if they match, false
    def __eq__(self, other):
        if self.make == other.make and self.color == other.color and self.year == other.year:
            return True
        return False

    # Overloaded str() method that returns the contents as (color year make)
    # tester order is color, year, make
    def __str__(self):
        return "{0}, {1}, {2}".format(self.color, self.year, self.make)
