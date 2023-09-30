import math

def triangle(s1, s2, s3):
    assert s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1

    s = (s1 + s2 + s3) / 2
    area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
    return area

s1 = float(input("Enter the length of side 1 : "))
s2 = float(input("Enter the length of side 2 : "))
s3 = float(input("Enter the length of side 3 : "))

print(triangle(s1, s2, s3))
