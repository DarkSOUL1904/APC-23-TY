# Write a PYTHON program to print the natural numbers up to n.

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i, end=" ")

# Write a PYTHON program to print even numbers up to n.

n = int(input("Enter n: "))

for i in range(2, n + 1, 2):
    print(i, end=" ")

# Write a PYTHON program to print odd numbers up to n.

n = int(input("Enter n: "))

for i in range(1, n + 1, 2):
    print(i, end=" ")

# Write a PYTHON program that prints 1 2 4 8 16 32 … n².

n = int(input("Enter n: "))

value = 1

while value <= n * n:
    print(value, end=" ")
    value *= 2

# Write a PYTHON program to sum the sequence 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!

n = int(input("Enter n: "))

sum_series = 1
fact = 1

for i in range(1, n + 1):
    fact *= i
    sum_series += 1 / fact

print("Sum =", sum_series)

# Write a PYTHON program to compute the cosine series.

x = float(input("Enter x: "))
n = int(input("Enter n: "))

sum = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1

    for j in range(1, i + 1):
        fact *= j

    sum += sign * (x ** i) / fact
    sign *= -1

print("cos(x) =", sum)

# Write a short PYTHON program to check whether the square root of a number is prime or not.

import math

n = int(input("Enter a number: "))
root = int(math.sqrt(n))

prime = True

if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

if prime:
    print("Square root is prime")
else:
    print("Square root is not prime")

# Write a PYTHON program to produce the following design.
# A B C
# A B C
# A B C

for i in range(3):
    for ch in ['A', 'B', 'C']:
        print(ch, end=" ")
    print()

# Write a PYTHON program to produce following design.
# A
# A B
# A B C
# A B C D
# A B C D E

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# Write a PYTHON program to produce following design.
# A B C D E
# A B C D
# A B C
# A B
# A

n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# Write a PYTHON program to produce following design.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Write a PYTHON program to produce following design.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()