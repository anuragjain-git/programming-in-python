#Q1

def str_to_int(num_str):
    if not num_str:
        return 0
    
    first = int(num_str[0])
    remaining = str_to_int(num_str[1:])
    
    return first * (10 ** len(num_str[1:])) + remaining

result = str_to_int('1234')
print(f'type of {result} is : {type(result)}')

#Q2

def sum_digits(n):
    return n if n < 10 else n % 10 + sum_digits(n // 10)
n = 1234
print(f'sum of digits of {n}: {sum_digits(n)}')

#Q3

def power(a, b):
    return 1 if b==0 else a * power(a, b-1)
a = 2
b = 3
print(f'{a}**{b} = {power(a, b)}')

#Q4

def harmonic_sum(n):
    return 1 if n == 1 else 1/n + harmonic_sum(n - 1)
n = 4
print(f'harmonic sum of {n} = {harmonic_sum(n)}')

#Q5

def geometric_sum(n, r):
    return 0 if n == 0 else (r ** (n - 1)) + geometric_sum(n-1, r)
n = 4
r = 1/2
print(f"geometric sum of first {n} terms and ratio {r} is {geometric_sum(n, r)}")

#Q6

def pos_int_sum(n):
    return 0 if n <= 0 else n + pos_int_sum(n-2)
n = 6
print(f'Positive integer sum of {n} is {pos_int_sum(n)}')

#Q7

def subset_sums(lst, index, current_sum, result):
    # Base case: when we reach the end of the array append current sum
    if index == len(lst):
        result.append(current_sum)
        return
    
    # Include the current element in the subset
    subset_sums(lst, index + 1, current_sum + lst[index], result)
    
    # Exclude the current element from the subset
    subset_sums(lst, index + 1, current_sum, result)
                
lst = [2, 3]
result = []
subset_sums(lst, 0, 0, result)
print("Input:", lst)
print("Output:", sorted(result))

#Q8

def is_prime(num, divisor=2):
    if num < 2:
        return False
    if divisor > (num // 2):
        return True
    if num % divisor == 0:
        return False
    return is_prime(num, divisor+1)
num=9
if is_prime(num):
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')

#Q9

def mul(a, b):
    if b==0:
        return 0
    return a + mul(a, b-1)
a=3
b=4
print(f'{a} * {b} = {mul(a, b)}')

#Q10

def strictly_increasing(num, start=0, curr_num=""):
    if num == 0:
        print(curr_num)
        return
    
    for digits in range(start, 10):
        str1 = curr_num + str(digits)
        strictly_increasing(num-1, digits+1, str1)
n=2
print(f'Strictly increasing {n} digit numbers:')
strictly_increasing(n)

#Q11

def binary_string(n, curr_str=""):
    if len(curr_str) == n:
        print(curr_str)
        return
    binary_string(n, curr_str+'0')
    binary_string(n, curr_str+'1')

n = 3
print(f'Binary strings of length {n}:')
binary_string(n)  

#Q12

def interleaving_strings(str1, str2, result=""):
    # if str1 and str2 is empty print and return
    if not str1 and not str2:
        print(result)
        return

    if str1:
        interleaving_strings(str1[1:], str2, result+str1[0])
    if str2:
        interleaving_strings(str1, str2[1:], result+str2[0])

str1="AB"
str2="CD"
print(f'Interleaving string of {str1} and {str2}: ')
interleaving_strings(str1,str2)

#Q13

def insert_x_at_kth_position(lst, element, position, index=0):
    if index==len(lst):
        return []
    elif (index + 1) % position == 0:
        return [lst[index], element] + insert_x_at_kth_position(lst, element, position, index+1)
    else:
        return [lst[index]] + insert_x_at_kth_position(lst, element, position, index+1)

lst=[1,2,3,4,5,6,7,8,9]
element=50
position=2
print(f'Insert {element} at every {position} position in the list : {lst}')
print('position counting (0,1,2,3)')
print(insert_x_at_kth_position(lst, element, position))

#Q14

def delete_every_kth_element(lst, position, index=0):
    if index==len(lst):
        return []
    elif (index+1) % position == 0:
        return delete_every_kth_element(lst, position, index+1)
    else:
        return [lst[index]] + delete_every_kth_element(lst, position, index+1)
lst=[1,2,3,4,5,6,7,8,9,10,11]
k=3
print(f'Delete every element at position {k} in the list: {lst}')
print('position counting (1,2,3)')
print(delete_every_kth_element(lst,k))

#Q15

def remove_adjacent_duplicate(lst):
    if len(lst)<=1:
        return lst
    elif lst[0] == lst[1]:
        return remove_adjacent_duplicate(lst[1:])
    else:
        return [lst[0]] + remove_adjacent_duplicate(lst[1:])
lst=[1,2,2,4,5,5,5,4]
print(f'removing duplicates from list : {lst}')
print(remove_adjacent_duplicate(lst))

#Q16

def gcd(a,b):
    return a if b==0 else gcd(b, a % b)
a=25
b=11
print(f'gcd of {a} and {b} is {gcd(a,b)}')



















