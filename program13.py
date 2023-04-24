from mymodule import addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = addition(num1, num2)
print("Addition of {} and {} is {}".format(num1, num2, result))