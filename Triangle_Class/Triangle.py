# This Triangle Class will

class Triangle:
    # constructor
    def __init__(self, side1=3, side2=4, side3=5):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # setters
    def setA(self, side1):
        self.side1 = side1

    def setB(self, side2):
        self.side2 = side2

    def setC(self, side3):
        self.side3 = side3

    # Getters
    def getA(self):
        return self.side1

    def getB(self):
        return self.side2

    def getC(self):
        return self.side3

    # other methods
    def isEquilateral(self):
        # all three sides are equal
        if self.side1 == self.side2 and self.side2 == self.side3:
            return True
        else:
            return False

    def isScalene(self):
        # at least two sides are equal (either just 2 or all 3)
        if self.side1 != self.side2 and self.side1 != self.side3 and self.side2 != self.side3:
            return True
        else:
            return False

    def isIsosceles(self):
        # no two sides are equal
        if self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return True
        else:
            return False

    def isRight(self):
        # the square of one of the sides is equal to the sum of the squares of the other two sides (You should check all three combinations)
        side1_sq = self.side1 * self.side1 == self.side2 * self.side2 + self.side3 * self.side3
        side2_sq = self.side2 * self.side2 == self.side1 * self.side1 + self.side3 * self.side3
        side3_sq = self.side3 * self.side3 == self.side2 * self.side2 + self.side1 * self.side1
        # a^2+b^2=c^2
        if side1_sq or side2_sq or side3_sq:
            return True
        else:
            return False
