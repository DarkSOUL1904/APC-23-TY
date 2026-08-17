# Question: Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.

student = {
    "roll_number": 101,
    "name": "Rahul",
    "department": "Computer Science",
    "marks": 85
}

# Display all key-value pairs
for key, value in student.items():
    print(key, ":", value)

# Question: Create a dictionary containing employee information and display the value associated with a specified key.

employee = {
    "id": 101,
    "name": "Amit",
    "department": "IT",
    "salary": 50000
}

key = "name"
print(employee[key])

# Question: Create a dictionary of five products and their prices. Add a new product and price to the dictionary.

products = {
    "Pen": 10,
    "Book": 50,
    "Pencil": 5,
    "Bag": 500,
    "Bottle": 100
}

products["Notebook"] = 80

print(products)

# Question: Create a dictionary containing student marks. Update the marks of a specified student.

marks ={
    "SAM": 90,
    "john": 80,
    "kam": 56 ,
}

marks["SAM"] = 99

print(marks)

# Question: Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
cities ={
    "kop": 95555,
    "pune": 100000,
    "mumbai": 200000,
}

del cities["mumbai"]

print(cities)


# Question: Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.

employees = {
    101: "Amit",
    102: "Rahul",
    103: "Priya",
    104: "Sneha",
    105: "Rohan"
}

employee_id = int(input("Enter employee ID: "))

if employee_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")

# Question: Create a dictionary containing student records and find the total number of key-value pairs.

students = {
    101: "Amit",
    102: "Rahul",
    103: "Priya",
    104: "Sneha",
    105: "Rohan"
}

print("Total number of key-value pairs:", len(students))

# Question: Create a dictionary and display:
# • All keys
# • All values
# • All key-value pairs

student = {
    "name": "Amit",
    "age": 20,
    "department": "IT",
    "marks": 85
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Key-value pairs:", student.items())

# Question: Create a dictionary of programming languages and their creators. Display each key and value using a loop.

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}

for language, creator in languages.items():
    print(language, ":", creator)


# Question: Accept five student names and their marks from the user and store them in a dictionary.

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print(students)

# Question: Create a dictionary containing student names and marks. Find the student who has scored the highest marks.

students = {
    "Amit": 85,
    "Rahul": 92,
    "Priya": 78,
    "Sneha": 95,
    "Rohan": 88
}

highest_student = max(students, key=students.get)

print(highest_student, ":", students[highest_student])

# Question: Create a dictionary containing student names and marks. Find the student with the lowest marks.

students = {
    "Amit": 85,
    "Rahul": 92,
    "Priya": 78,
    "Sneha": 95,
    "Rohan": 88
}

lowest_student = min(students, key=students.get)

print(lowest_student, ":", students[lowest_student])

# Question: Create a dictionary containing student names and marks. Calculate the average marks of all students.

students = {
    "Amit": 85,
    "Rahul": 92,
    "Priya": 78,
    "Sneha": 95,
    "Rohan": 88
}

average = sum(students.values()) / len(students)

print("Average marks:", average)

# Question: Accept a string from the user and create a dictionary containing each character and its frequency.

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)

# Question: Accept a sentence and create a dictionary containing each word and the number of times it occurs.

sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

# Question: Create two dictionaries and merge them into a single dictionary.

dict1 = {
    "a": 10,
    "b": 20
}

dict2 = {
    "c": 30,
    "d": 40
}

merged_dict = {**dict1, **dict2}

print(merged_dict)

# Question: Given two dictionaries, find the keys that are common to both dictionaries.

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "b": 40,
    "c": 50,
    "d": 60
}

common_keys = dict1.keys() & dict2.keys()

print(common_keys)


# Question: Given two dictionaries, identify the values that are common to both dictionaries.

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "x": 20,
    "y": 30,
    "z": 40
}

common_values = set(dict1.values()) & set(dict2.values())

print(common_values)

# Question: Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.

data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

unique_data = {}

for key, value in data.items():
    if value not in unique_data.values():
        unique_data[key] = value

print(unique_data)

# Question: Create a dictionary and display its elements in ascending order of keys.

data = {
    5: "E",
    2: "B",
    4: "D",
    1: "A",
    3: "C"
}

for key in sorted(data):
    print(key, ":", data[key])


# Question: Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.

squares = {}

for i in range(1, 11):
    squares[i] = i ** 2

print(squares)

# Question: Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.

squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i ** 2

print(squares)

# Question: Given a list of numbers, create a dictionary containing each unique number and its frequency.

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)

# Question: Create a dictionary containing integers from 1 to 10 and their cubes.

cubes = {}

for i in range(1, 11):
    cubes[i] = i ** 3

print(cubes)

# Question: Create a dictionary containing student names and marks. Develop a program to:
# • Add a student
# • Update marks
# • Delete a student
# • Search for a student
# • Display all students
# • Find the highest marks
# • Calculate the average

students = {
    "Amit": 85,
    "Rahul": 92,
    "Priya": 78
}

students["Sneha"] = 95

students["Amit"] = 90

del students["Priya"]

name = "Rahul"
if name in students:
    print("Student found:", name, students[name])
else:
    print("Student not found")

print("All students:")
for name, marks in students.items():
    print(name, ":", marks)

highest_student = max(students, key=students.get)
print("Highest marks:", highest_student, students[highest_student])

average = sum(students.values()) / len(students)
print("Average marks:", average)

# Question: Create a dictionary containing employee names and salaries. Find:
# • Highest salary
# • Lowest salary
# • Average salary
# • Employees earning more than ₹50,000

employees = {
    "Amit": 45000,
    "Rahul": 60000,
    "Priya": 55000,
    "Sneha": 75000,
    "Rohan": 40000
}

highest_salary = max(employees.values())
lowest_salary = min(employees.values())
average_salary = sum(employees.values()) / len(employees)

print("Highest salary:", highest_salary)
print("Lowest salary:", lowest_salary)
print("Average salary:", average_salary)

print("Employees earning more than ₹50,000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)

# Question: Create a dictionary containing product names and quantities.
# Perform:
# • Add a product
# • Update quantity
# • Delete a product
# • Search for a product
# • Display products with quantity below 10

products = {
    "Pen": 15,
    "Book": 8,
    "Pencil": 20,
    "Bag": 5,
    "Bottle": 12
}

products["Notebook"] = 10

products["Pen"] = 25

del products["Bottle"]

product = "Book"
if product in products:
    print("Product found:", product, products[product])
else:
    print("Product not found")

print("Products with quantity below 10:")
for product, quantity in products.items():
    if quantity < 10:
        print(product, ":", quantity)


# Question: Create a dictionary containing names and phone numbers.
# Implement:
# • Add contact
# • Search contact
# • Update contact
# • Delete contact
# • Display all contacts

contacts = {
    "Amit": "9876543210",
    "Rahul": "9876501234",
    "Priya": "9876512345"
}

contacts["Sneha"] = "9876523456"

name = "Rahul"
if name in contacts:
    print("Contact found:", contacts[name])
else:
    print("Contact not found")

contacts["Amit"] = "9999999999"

del contacts["Priya"]

print("All contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)


# Question: Create a dictionary containing book IDs and book names.
# Implement:
# • Add a book
# • Search a book
# • Remove a book
# • Display all books
# • Count total books

books = {
    101: "Python Programming",
    102: "Data Structures",
    103: "Computer Networks"
}

books[104] = "Database Management"

book_id = 102
if book_id in books:
    print("Book found:", books[book_id])
else:
    print("Book not found")

del books[103]

print("All books:")
for book_id, book_name in books.items():
    print(book_id, ":", book_name)

print("Total books:", len(books))


# Question: Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.

students = {
    "Amit": "Computer Science",
    "Rahul": "Mechanical",
    "Priya": "Computer Science",
    "Sneha": "Electronics",
    "Rohan": "Mechanical"
}

grouped = {}

for name, department in students.items():
    if department not in grouped:
        grouped[department] = []
    grouped[department].append(name)

print(grouped)


# Question: Take a list of words, create a dictionary where the key is the word length and the value is a list of words having that length.

words = ["cat", "dog", "apple", "bat", "mango", "sun"]

grouped = {}

for word in words:
    length = len(word)
    if length not in grouped:
        grouped[length] = []
    grouped[length].append(word)

print(grouped)


# Question: Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.

numbers = [2, 7, 11, 15]
target = 9

seen = {}

for num in numbers:
    complement = target - num

    if complement in seen:
        print("Numbers:", complement, "and", num)
        break

    seen[num] = True


# Question: Take a string, use a dictionary to find the first character that occurs only once.

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No unique character found")


# Question: Take a string, use a dictionary to find the first character that occurs more than once.

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] > 1:
        print("First repeating character:", char)
        break
else:
    print("No repeating character found")

# Question: Accept a paragraph and create a dictionary where:
# • Key = word length
# • Value = number of words having that length.

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
word_lengths = {}

for word in words:
    length = len(word)
    word_lengths[length] = word_lengths.get(length, 0) + 1

print(word_lengths)




