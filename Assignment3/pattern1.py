def p1(n):

    for i in range (1,n):
        for j in range (1, i+1):
            print(j," ",end='')
        print()

#p1(6)

def p2(n):
    for i in range(1, n + 1):
        print("  " * (n - i), end='')
        if i == 1:
            s = str(i)
        else:
            s=(f'{i} {s} {i}')
        print(s)
        
#p2(4)

def p3(n):
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j," ", end='')
        print()

#p3(6)

def p4(n):
    for i in range(1,n):
        for j in range(1, i+1):
            print(f'{i} ', end='')
        print()

#p4(6)

def p5(n):
    for i in range(1,n+1):
        print("  " * (i - 1), end='')
        for j in range(i, n+1):
            print(f'{j} ', end='')
        print()

#p5(5)

def p6(n):
    for i in range(1,n+1):
        for j in range(1, n+1):
            if(i == 1 or i == n or j == 1 or j== n):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

#p6(5)

def p7(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("* ",end="")
        print()

p7(6)
