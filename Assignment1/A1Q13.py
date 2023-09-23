import math

height = int (input("Enter the height from which the object is dropped : "))
vi = int (input("Enter initial velocity : "))

vf = math.sqrt(((vi*vi) + 2*9.8*height))

print(vf)
