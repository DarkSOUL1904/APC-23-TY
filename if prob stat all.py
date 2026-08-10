# Write a PYTHON program that reads a value of n and checks whether the number is zero or non-zero.

n = int(input("Enter a number: "))

if n == 0:
    print("Zero")
else:
    print("Non-Zero")

# Write a PYTHON program to find the largest of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number =", a)
else:
    print("Largest number =", b)

# Write a PYTHON program that reads a number and checks whether the number is positive or negative.

n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Write a PYTHON program to check whether the entered character is a vowel or consonant.

ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# Write a PYTHON program to evaluate the student performance.

percentage = float(input("Enter percentage: "))

if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Poor performance")

# Write a PYTHON program to find the largest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number =", a)
elif b >= a and b >= c:
    print("Largest number =", b)
else:
    print("Largest number =", c)

# Write a PYTHON program to find the smallest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest number =", a)
elif b <= a and b <= c:
    print("Smallest number =", b)
else:
    print("Smallest number =", c)

# Write a PYTHON program to check whether a number is even or odd.

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Write a PYTHON program to check a year for leap year.

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Write a PYTHON program to determine whether the driver is insured or not.

marital_status = input("Enter marital status (married/unmarried): ").lower()

if marital_status == "married":
    print("Driver is insured")
else:
    gender = input("Enter gender (male/female): ").lower()
    age = int(input("Enter age: "))

    if (gender == "male" and age > 30) or (gender == "female" and age > 25):
        print("Driver is insured")
    else:
        print("Driver is not insured")