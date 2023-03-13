# write program to find gcd and lcm of two numbers.
import math as m
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD of", a, "and", b, "is", m.gcd(a, b))
print("LCM of", a, "and", b, "is", (a*b)/m.gcd(a, b))

# write program to find gcd and lcm of two numbers using euclidean algorithm.
import math as m
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def gcd(a, b):
    while(b):
        if(a < b):
            a,b=b,a
        a,b=b,a%b
    return a
print("GCD of", a, "and", b, "is", m.gcd(a, b))
print("LCM of", a, "and", b, "is", (a*b)/m.gcd(a, b))