#Sandi Jasmer Lab 1 Functions

#Write a function with two parameters, a and b.
# It returns true if a is a power of b. That is, if there is some number n such that 𝒂 =𝒃𝒏.
# For example, 27 is a power of 3 since 27 = 3^3 , but 27 is not a power of 9;
# 16 is a power of 4 since 16= 42, 16 is also a power of 2 since 16 = 24,
# but 16 is not a power of 8, even though it is a multiple of 8.
#Remember to check for the two default causes (a is a power of a and 1 is a power of a).
def pow_testers(a,b):
    # You are to use the following algorithm: a is a power of b, if a is divisible by b and a/b is divisible by b.
    if b==a or a==1:
        return True
    elif a%b==0 and (a/b)%b==0:
        return True
    else:
        return False
print("This program will return True if the A is the power of b, otherwise it will return false.")


#testers
print("Expecting True for a=5 and b=5")
print(pow_testers(5,5))

print("Expecting True for a=25 and b=5")
print(pow_testers(25,5))

print("Expecting False for a=125 and b=25")
print(pow_testers(125,25))

print("Expecting True for a=1 and b=13")
print(pow_testers(1,13))

print("Expecting True for a=64 and b=4")
print(pow_testers(64,4))

print("Expecting False for a=27 and b=9")
print(pow_testers(27,9))

print("Expecting True for a=256 and b=2")
print(pow_testers(256,2))

