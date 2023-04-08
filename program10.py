class calculator:
    def add(self, a,b):
        return  a+b
object = calculator()
num1 = float(input("Enter the number of elements in the list: "))
num2 = float(input("Enter the number of elements in the list: "))
result = object.add(num1, num2)
print("Addition of two number is: ", result)