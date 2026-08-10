# Create a list of five fruits and display the list.

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(fruits)

# Create a list of five integers. Display first, last and third element.

numbers = [10, 20, 30, 40, 50]

print("First:", numbers[0])
print("Last:", numbers[-1])
print("Third:", numbers[2])

# Replace the third color with another color.

colors = ["Red", "Blue", "Green", "Yellow"]
colors[2] = "Purple"
print(colors)

# Add elements at end, beginning and specified position.

numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(0, 5)
numbers.insert(2, 15)

print(numbers)

# Remove first, last and specific student.

students = ["Amit", "Ravi", "Neha", "Priya", "Kiran"]

students.pop(0)
students.pop()
students.remove("Neha")

print(students)

# Find largest and smallest number in a list.

numbers = [12, 45, 8, 67, 23]

largest = smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)

# Accept 10 numbers and calculate sum and average.

numbers = []

for i in range(10):
    numbers.append(int(input("Enter number: ")))

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

# Count even and odd numbers.

numbers = []

for i in range(15):
    numbers.append(int(input("Enter number: ")))

even = odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)

# Check whether city exists in list.

cities = ["Pune", "Mumbai", "Delhi", "Kolhapur"]

city = input("Enter city: ")

if city in cities:
    print("City Found")
else:
    print("City Not Found")

# Reverse a list without reverse().

numbers = [10, 20, 30, 40, 50]

reversed_list = numbers[::-1]

print(reversed_list)

# Display first 5, last 5, middle 4, alternate and reverse elements.

numbers = [1,2,3,4,5,6,7,8,9,10]

print("First 5:", numbers[:5])
print("Last 5:", numbers[-5:])
print("Middle 4:", numbers[3:7])
print("Alternate:", numbers[::2])
print("Reverse:", numbers[::-1])

# Display elements at even index positions.

numbers = [10,20,30,40,50,60]

print(numbers[::2])

# Sort numbers in ascending and descending order.

numbers = []

for i in range(10):
    numbers.append(int(input("Enter number: ")))

print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))

# Display unique elements.

numbers = [1,2,2,3,4,4,5,6,6]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

# Find second largest element.

numbers = [10, 20, 30, 40, 50]

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest:", second)

# Store and display student details.

students = [
    ["Amit", 1, 85],
    ["Ravi", 2, 78],
    ["Neha", 3, 90]
]

for student in students:
    print(student)

# Add two 3x3 matrices.

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

C = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    C.append(row)

for row in C:
    print(row)

# Shopping cart operations.

cart = ["Milk", "Bread"]

cart.append("Butter")
cart.remove("Bread")

item = "Milk"

if item in cart:
    print("Found")

print(cart)
print("Total Items:", len(cart))

# Student attendance operations.

students = ["Amit", "Ravi", "Neha"]

print("Total Students:", len(students))

name = input("Search student: ")

if name in students:
    print("Present")

students.append("Priya")
students.remove("Ravi")

print(students)

# Book management.

books = ["Python", "Java", "C++"]

books.append("HTML")

book = input("Search book: ")

if book in books:
    print("Book Found")

books.remove("Java")

print(books)
print("Total Books:", len(books))

# Merge two lists.

list1 = [1,2,3]
list2 = [4,5,6]

merged = list1 + list2

print(merged)

# Find common elements between two lists.

list1 = [1,2,3,4]
list2 = [3,4,5,6]

common = []

for item in list1:
    if item in list2:
        common.append(item)

print(common)

# Count frequency of each element.

numbers = [1,2,2,3,3,3,4]

for num in set(numbers):
    print(num, ":", numbers.count(num))

# Rotate list left and right.

numbers = [1,2,3,4,5]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("Left Rotation:", left)
print("Right Rotation:", right)

# Remove duplicates preserving order.

numbers = [1,2,2,3,4,3,5]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print(result)

# Analyze student marks.

marks = [60,70,80,90,75,85,95,55,65,88,77,66,99,45,58,73,81,92,68,79]

average = sum(marks)/len(marks)

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", average)

above = below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("Above Average:", above)
print("Below Average:", below)

# Analyze employee salaries.

salaries = [25000,30000,55000,70000,45000,60000]

print("Highest:", max(salaries))
print("Lowest:", min(salaries))
print("Average:", sum(salaries)/len(salaries))

for salary in salaries:
    if salary > 50000:
        print("Above 50000:", salary)

for salary in salaries:
    if salary < 30000:
        print("Below 30000:", salary)

# Analyze batsman scores.

scores = [45,67,120,88,150,99,55,101,34,76]

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total:", sum(scores))
print("Average:", sum(scores)/len(scores))

century = 0
half = 0

for score in scores:
    if score >= 100:
        century += 1
    elif score >= 50:
        half += 1

print("Centuries:", century)
print("Half Centuries:", half)

# Analyze temperatures.

temp = [30,31,29,35,36,33,32,34,28,27]

average = sum(temp)/len(temp)

print("Hottest:", max(temp))
print("Coldest:", min(temp))
print("Average:", average)

for t in temp:
    if t > average:
        print("Above Average:", t)

for t in temp:
    if t < average:
        print("Below Average:", t)

# Patient management.

patients = ["Ram", "Shyam"]

patients.append("Amit")

name = input("Search patient: ")

if name in patients:
    print("Patient Found")

patients.remove("Shyam")

print(patients)
print("Total Patients:", len(patients))