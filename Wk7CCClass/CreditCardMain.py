from Person import Person

# uncomment this line to test CreditCard
from CreditCard import CreditCard


def main():
    # begin PERSON_TEST
    print("\nPerson Test")
    bob = Person()
    marge = Person("Marge", "Inovera", "321 Stats Lane")

    print("Displaying Bob (all should be blank)")
    print(" First Name: " + bob.getFirstName(), end=", ")
    print("Last Name: " + bob.getLastName(), end=", ")
    print("Address: " + bob.getAddress())

    print("\nMarge, expected output is")
    print(" First Name: Marge, Last Name: Inovera, Address: 321 Stats Lane")
    print("Actual Result")
    print(" First Name: " + marge.getFirstName(), end=", ")
    print("Last Name: " + marge.getLastName(), end=", ")
    print("Address: " + marge.getAddress())

    # end PERSON_TEST

    # begin CC_TEST
    print("\n\nCredit Card Test")
    try:
        discover = CreditCard("Lou", "Pole", "456 Haven Ave", 8675309, 5000)
        print("Card Number - Expected: 8675309, Actual: " + str(discover.getCardNumber()))
        print("Card Holder Name - Expected: Lou Pole, Actual: " + discover.getOwnerName())
        print("Address - Expected: 456 Haven Ave, Actual: " + discover.getAddress())
        print("Credit Limit - Expected: 5000, Actual: " + str(discover.getCreditLimit()))
        print("Balance - Expected: 0, Actual: " + str(discover.getBalance()))

        if discover.makeCharge(3000):
            print("\nCharge of 3000 applied correctly")
        else:
            print("\nCharge failed")
        print("Balance - Expected: 3000, Actual: " + str(discover.getBalance()))

        if discover.makeCharge(4000):
            print("\nAdditional Charge of 4000 allowed in error")
        else:
            print("\nCard declined correctly")
        print("Balance - Expected: 3000, Actual: " + str(discover.getBalance()))

        if discover.makeCharge(-500):
            print("\nNegative charge allowed in error")
        else:
            print("\nNegative charge denied correctly")
        print("Balance - Expected: 3000, Actual: " + str(discover.getBalance()))

        if discover.payBalance(400):
            print("\nPayment of 400 accepted correctly")
        else:
            print("\nPayment denied in error")
        print("Balance - Expected: 2600, Actual: " + str(discover.getBalance()))

        if discover.payBalance(-500):
            print("\nNegative payment accepted in error")
        else:
            print("\nNegative payment denied correctly")
        print("Balance - Expected: 2600, Actual: " + str(discover.getBalance()))

        print("\nNow setting credit limit to 10000")
        discover.setCreditLimit(10000)
        print("Credit Limit - Expected: 10000, Actual: " + str(discover.getCreditLimit()))

        if discover.makeCharge(4000):
            print("\nAdditional charge of 4000 applied correctly")
        else:
            print("\nCharge denied in error")
        print("Balance - Expected: 6600, Actual: " + str(discover.getBalance()))

        if discover.setCreditLimit(5000):
            print("\nCredit Limit reduced below current balance correctly.")
        else:
            print("Balance modification failed in error")
        print("Credit Limit - Expected: 5000, Actual: " + str(discover.getCreditLimit()))
        print("Balance - Expected: 6600, Actual: " + str(discover.getBalance()))

        if discover.makeCharge(5):
            print("\nAdditional Charge of 5 allowed in error")
        else:
            print("\nCard declined correctly")
        print("Balance - Expected: 6600, Actual: " + str(discover.getBalance()))

        if discover.payBalance(7000):
            print("\nPayment of 7000 accepted correctly")
        else:
            print("\nPayment denied in error")
        print("Balance - Expected: -400, Actual: " + str(discover.getBalance()))
    except NameError:
        print("Credit Card not implemented")


# end CC_TEST

if __name__ == '__main__':
    main()
