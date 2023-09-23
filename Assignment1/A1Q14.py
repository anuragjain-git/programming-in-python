

num = int (input("Enter four digit integer : "))

res = 0

res = res + (num%10)
print(num%10)
num = num//10

res = res + (num%10)
print(num%10)
num = num//10

res = res + (num%10)
print(num%10)
num = num//10

res = res + (num%10)
print(num%10)


print(res)
