import math

a = int (input("Enter the value of a : "))
b = int (input("Enter the value of b : "))
c = int (input("Enter the value of c : "))

print((-b + math.sqrt((b*b) - 4 * a * c)) / 2 * a);

x = int (input("Enter the value of x : "))
y = int (input("Enter the value of y : "))

print((((2 * x * y)- 9* y) / 2 * x * y * y * y) - ((4 * y * x * x) / 2 * y))

v = int (input("Enter the value of v : "))

print((2 * math.cos(0.5 * (x + y))) * math.cos(0.5 * (x - y)) + math.exp(x) -1 - (x / 4) + math.tan(x) - math.log(v))
