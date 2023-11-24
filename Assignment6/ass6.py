def f1(w):
    r = w[0]
    for i in range(1, len(w)):
        r += "*" if r[-1] == w[i] else w[i]
    return r
print(f1("balloon"))



def f2(a,b):
    return (sorted(a) == sorted(b))
print(f2("abc","acb"))



def f3(s):
    return len(s.split())
print(f3("i am anurag jain"))



def f4(s):
    res = chr(ord(s[0]) - 32) if 'a' <= s[0] <= 'z' else s[0]
    for i in range(1, len(s)):
        if s[i - 1] == ' ' and 'a' <= s[i] <= 'z':
            res += chr(ord(s[i]) - 32)
        elif s[i - 1] != ' ' and 'A' <= s[i] <= 'Z':
            res += chr(ord(s[i]) + 32)
        else:
            res += s[i]
    return res

print(f4("i aM ANUrag jaiN"))



import re
def f5(s):
    pattern = r'\b[A-Za-z]+\b'
    return len(re.findall(pattern, s))

print(f5("88 Anurag jain02 "))





