# Write a PYTHON program to print the natural numbers up to n.

n = int(input("Enter n: "))

i = 1

while i <= n:
    print(i, end=" ")
    i += 1

# Write a PYTHON program to print even numbers up to n.

n = int(input("Enter n: "))

i = 2

while i <= n:
    print(i, end=" ")
    i += 2

# Write a PYTHON program to print odd numbers up to n.

n = int(input("Enter n: "))

i = 1

while i <= n:
    print(i, end=" ")
    i += 2

# Write a PYTHON program to print sum of natural numbers up to n.

n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print("Sum =", sum)

# Write a PYTHON program to print sum of odd numbers up to n.

n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum += i
    i += 2

print("Sum =", sum)


# Write a PYTHON program to print sum of even numbers up to n.

n = int(input("Enter n: "))

i = 2
sum = 0

while i <= n:
    sum += i
    i += 2

print("Sum =", sum)

# Write a PYTHON program to print natural numbers up to n in reverse order.

n = int(input("Enter n: "))

while n >= 1:
    print(n, end=" ")
    n -= 1

    # Write a PYTHON program to print Fibonacci series up to n.

n = int(input("Enter n: "))

a = 0
b = 1

while a <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c

    # Write a PYTHON program to find factorial of a given number.

n = int(input("Enter a number: "))

fact = 1

while n > 0:
    fact *= n
    n -= 1

print("Factorial =", fact)

# Write a PYTHON program to check the entered number is prime or not.

n = int(input("Enter a number: "))

prime = True

if n < 2:
    prime = False
else:
    i = 2
    while i < n:
        if n % i == 0:
            prime = False
            break
        i += 1

if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")


# Write a PYTHON program to find the sum of digits of a given number.

n = int(input("Enter a number: "))

sum = 0

while n > 0:
    sum += n % 10
    n //= 10

print("Sum of digits =", sum)

# Write a PYTHON program to check the entered number is palindrome or not.

n = int(input("Enter a number: "))

temp = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if temp == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# Write a PYTHON program to reverse the given number.

n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reversed Number =", reverse)

# Write a PYTHON program to print the multiplication table.

n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1



# Write a PYTHON program to print the largest of n numbers.

n = int(input("Enter how many numbers: "))

largest = int(input("Enter number 1: "))

i = 2

while i <= n:
    num = int(input("Enter number: "))
    
    if num > largest:
        largest = num
        
    i += 1

print("Largest number =", largest)

# Write a PYTHON program to print the smallest of n numbers.

n = int(input("Enter how many numbers: "))

smallest = int(input("Enter number 1: "))

i = 2

while i <= n:
    num = int(input("Enter number: "))
    
    if num < smallest:
        smallest = num
        
    i += 1

print("Smallest number =", smallest)