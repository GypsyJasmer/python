# a CreditCard class that contains information about a credit account,
# and a Person class which contains basic biographical information about a person.

class Person:
    # Initialization
    # each of which defaults to an empty string
    def __init__(self, first_name="", last_name="", address=""):
        self._first_name = first_name
        self._last_name = last_name
        self._address = address

    # setters
    def setFirst_name(self, first_name):
        self._first_name = first_name

    def setLast_name(self, last_name):
        self._last_name = last_name

    def setAddress(self, address):
        self._address = address

    # getters
    def getFirstName(self):
        return self._first_name

    def getLastName(self):
        return self._last_name

    def getAddress(self):
        return self._address
