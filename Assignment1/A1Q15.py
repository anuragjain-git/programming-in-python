import math

num1 = int (input("Enter an integer : "))
num2 = int (input("Enter an integer : "))
num3 = int (input("Enter an integer : "))

print(max(num1,num2,num3))
print(num1 + num2 + num3 - max(num1,num2,num3) - min(num1,num2,num3))
print(min(num1,num2,num3))
