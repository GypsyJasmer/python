
#For this lab, any exponent less than 0 should return 1 as its default behavior.
def pow_rec(base, power):
    #base case
    if power<=0:
        return 1
    elif power % 2==0: #if power is an even number
        return pow_rec(base, power/2)**2
    #recursive call not less than or equal to zero, not even and number is odd
    return base*pow_rec(base, power-1)




#testers
print("Expecting return value of 5")
print(pow_rec(5,1))

print("Expecting return value of 8192")
print(pow_rec(2,13))

print("Expecting return value of 729")
print(pow_rec(3,6))

print("Expecting return value of 390625")
print(pow_rec(5,8))

print("Expecting return value of 1")
print(pow_rec(27,0))

print("Expecting return value of 1")
print(pow_rec(13,-1))