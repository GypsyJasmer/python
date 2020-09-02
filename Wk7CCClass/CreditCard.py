# Each card will have a card number, balance, credit limit and an account owner
# a CreditCard class that contains information about a credit account,
# and a Person class which contains basic biographical information about a person.

from Person import Person


class CreditCard:
    # Initialization
    def __init__(self, first_name, last_name, address, card_number=0, cc_limit=0):
        self.card_number = card_number
        self.cc_limit = cc_limit
        self.balance = 0
        self._person = Person(first_name, last_name, address)

    # returns the current card balance
    def getBalance(self):
        return self.balance

    # returns the card number
    def getCardNumber(self):
        return self.card_number

    # returns the first and last name of the card owner from the associated Person
    def getOwnerName(self):
        return self._person.getFirstName() + " " + self._person.getLastName()

    # returns the card holder’s address
    def getAddress(self):
        return self._person.getAddress()

    # takes a value as an argument and applies that payment to the balance.
    # Payments must be non-negative values, but a negative balance is acceptable.
    # This function should return a Boolean value: true if the payment was applied
    # and false if it was not (due to negative payment amount).
    def payBalance(self, payment):
        if payment > 0:
            # apply payment to balance
            self.balance = self.balance - payment
            return True
        return False

    # takes a value and charges that amount to the card, increasing the balance.
    # Charges must be positive and cannot cause the balance to exceed the credit limit.
    # This function should return a Boolean: true if the charge was applied, false otherwise
    def makeCharge(self, charge):
        # balance after charge needs to be less then limit
        if charge > 0 and self.balance + charge < self.cc_limit:
            # applying charge
            self.balance = self.balance + charge
            return True
        return False

    # takes a value and sets the credit limit to a new value. Note that the credit
    # limit may be set to a value that is below the current balance,
    # but it cannot be set to a negative value. Return true if this succeeds, false if it fails.
    def setCreditLimit(self, cc_limit):
        if cc_limit > 0:
            self.cc_limit = cc_limit
            return True
        return False

    # returns the current credit limit.
    def getCreditLimit(self):
        return self.cc_limit
