x = int (input("Enter the value of x : "))
y = int (input("Enter the value of y : "))
z = int (input("Enter the value of z : "))
print(x < y)
print(not(z == y))
print(z < x)
print((x < y) or (not(z == y)and(z < x)))