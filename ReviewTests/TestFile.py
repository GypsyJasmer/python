def temp_conversion(keyword, temp):
    if keyword == "F2C":
        #changes temp from F to cel
        changed_temp = (temp - 32) * 5 / 9
    else:
        #changes temp from Cel to F
        changed_temp = (temp * 9 / 5) + 32
    return changed_temp


def main():
    print("Expecting the conversion for be 212F to 100C or visa versa")
    print(temp_conversion("F2C", 212))
    print(temp_conversion("C2F", 100))
    print("Expecting the conversion to be 32F to 0C or visa versa")
    print(temp_conversion("F2C", 32))
    print(temp_conversion("C2F", 0))
    print("Expecting the conversion to be -40F to -40C or visa versa")
    print(temp_conversion("F2C", -40))
    print(temp_conversion("C2F", -40))


if __name__ == "__main__":
    main()
