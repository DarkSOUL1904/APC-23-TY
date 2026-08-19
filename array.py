# ================================================================
# PYTHON PROGRAM
# SETS, DICTIONARIES AND ARRAY MODULE METHODS
# ================================================================

from array import array
import os


# ================================================================
# ARRAY MODULE METHODS
# This function demonstrates all required array methods.
# It is called after every question.
# ================================================================

def array_module_methods():

    print("\n--- ARRAY MODULE METHODS DEMONSTRATION ---")

    # ------------------------------------------------------------
    # append()
    # Adds one element at the end of an array.
    # ------------------------------------------------------------
    arr = array('i', [10, 20, 30])
    arr.append(40)
    print("append():", arr)

    # ------------------------------------------------------------
    # buffer_info()
    # Returns memory address and number of elements.
    # ------------------------------------------------------------
    print("buffer_info():", arr.buffer_info())

    # ------------------------------------------------------------
    # byteswap()
    # Swaps the byte order of every element.
    # ------------------------------------------------------------
    byte_arr = array('i', [1, 2, 3])
    byte_arr.byteswap()
    print("byteswap():", byte_arr)

    # ------------------------------------------------------------
    # count()
    # Counts occurrences of a specified element.
    # ------------------------------------------------------------
    count_arr = array('i', [10, 20, 10, 30, 10])
    print("count(10):", count_arr.count(10))

    # ------------------------------------------------------------
    # extend()
    # Adds multiple elements to the end.
    # ------------------------------------------------------------
    extend_arr = array('i', [1, 2, 3])
    extend_arr.extend([4, 5, 6])
    print("extend():", extend_arr)

    # ------------------------------------------------------------
    # frombytes()
    # Adds elements from a bytes object.
    # ------------------------------------------------------------
    original = array('i', [100, 200])
    byte_data = original.tobytes()

    from_bytes_arr = array('i')
    from_bytes_arr.frombytes(byte_data)
    print("frombytes():", from_bytes_arr)

    # ------------------------------------------------------------
    # fromfile()
    # Reads elements from a binary file.
    # ------------------------------------------------------------
    filename = "array_temp.bin"

    file_arr = array('i', [10, 20, 30])

    with open(filename, "wb") as file:
        file_arr.tofile(file)

    from_file_arr = array('i')

    with open(filename, "rb") as file:
        from_file_arr.fromfile(file, len(file_arr))

    print("fromfile():", from_file_arr)

    # ------------------------------------------------------------
    # fromlist()
    # Adds elements from a Python list.
    # ------------------------------------------------------------
    list_arr = array('i')
    list_arr.fromlist([5, 10, 15])
    print("fromlist():", list_arr)

    # ------------------------------------------------------------
    # fromunicode()
    # Adds characters from a Unicode string.
    # Requires Unicode array type 'u'.
    # ------------------------------------------------------------
    unicode_arr = array('u')
    unicode_arr.fromunicode("ABC")
    print("fromunicode():", unicode_arr)

    # ------------------------------------------------------------
    # index()
    # Returns the index of the first occurrence.
    # ------------------------------------------------------------
    index_arr = array('i', [10, 20, 30, 40])
    print("index(30):", index_arr.index(30))

    # ------------------------------------------------------------
    # insert()
    # Inserts an element at a specified position.
    # ------------------------------------------------------------
    insert_arr = array('i', [10, 20, 30])
    insert_arr.insert(1, 15)
    print("insert():", insert_arr)

    # ------------------------------------------------------------
    # pop()
    # Removes and returns an element.
    # ------------------------------------------------------------
    pop_arr = array('i', [10, 20, 30])
    removed = pop_arr.pop()
    print("pop():", removed)
    print("Array after pop():", pop_arr)

    # ------------------------------------------------------------
    # remove()
    # Removes the first occurrence of an element.
    # ------------------------------------------------------------
    remove_arr = array('i', [10, 20, 30, 20])
    remove_arr.remove(20)
    print("remove():", remove_arr)

    # ------------------------------------------------------------
    # reverse()
    # Reverses the array.
    # ------------------------------------------------------------
    reverse_arr = array('i', [1, 2, 3, 4, 5])
    reverse_arr.reverse()
    print("reverse():", reverse_arr)

    # ------------------------------------------------------------
    # tobytes()
    # Converts the array into bytes.
    # ------------------------------------------------------------
    bytes_arr = array('i', [10, 20, 30])
    byte_result = bytes_arr.tobytes()
    print("tobytes():", byte_result)

    # ------------------------------------------------------------
    # tofile()
    # Writes array elements to a binary file.
    # ------------------------------------------------------------
    output_arr = array('i', [100, 200, 300])

    with open(filename, "wb") as file:
        output_arr.tofile(file)

    print("tofile(): Data written to", filename)

    # ------------------------------------------------------------
    # tolist()
    # Converts an array into a Python list.
    # ------------------------------------------------------------
    tolist_arr = array('i', [10, 20, 30])
    print("tolist():", tolist_arr.tolist())

    # ------------------------------------------------------------
    # tounicode()
    # Converts a Unicode array into a string.
    # ------------------------------------------------------------
    unicode_array = array('u', ['P', 'y', 't', 'h', 'o', 'n'])
    print("tounicode():", unicode_array.tounicode())

    # Delete temporary file
    if os.path.exists(filename):
        os.remove(filename)

    print("--- END OF ARRAY METHODS ---")


# ================================================================
#                       SET QUESTIONS
# ================================================================


# ================================================================
# SET QUESTION 1
# Create a set containing five integers and display all elements.
# ================================================================

print("\n\n========== SET QUESTION 1 ==========")

numbers = {10, 20, 30, 40, 50}

print("Set elements:")
for number in numbers:
    print(number)

array_module_methods()


# ================================================================
# SET QUESTION 2
# Create a list containing duplicate values.
# Convert the list into a set.
# ================================================================

print("\n\n========== SET QUESTION 2 ==========")

numbers_list = [10, 20, 20, 30, 30, 40, 50, 50]

numbers_set = set(numbers_list)

print("Original List:", numbers_list)
print("Set after removing duplicates:", numbers_set)

array_module_methods()


# ================================================================
# SET QUESTION 3
# Create a set of five fruits.
# Add two new fruits.
# ================================================================

print("\n\n========== SET QUESTION 3 ==========")

fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

fruits.add("Pineapple")
fruits.add("Watermelon")

print("Updated fruit set:", fruits)

array_module_methods()


# ================================================================
# SET QUESTION 4
# Create a set of numbers and remove a specified number.
# ================================================================

print("\n\n========== SET QUESTION 4 ==========")

numbers = {10, 20, 30, 40, 50}

number_to_remove = 30

numbers.remove(number_to_remove)

print("Set after removing", number_to_remove, ":", numbers)

array_module_methods()


# ================================================================
# SET QUESTION 5
# Create a set of student names.
# Ask the user for a name and check whether it exists.
# ================================================================

print("\n\n========== SET QUESTION 5 ==========")

students = {"Rahul", "Amit", "Sneha", "Priya", "Rohan"}

name = input("Enter student name: ")

if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist in the set.")

array_module_methods()


# ================================================================
# SET QUESTION 6
# Create a set of cities and find total number of cities.
# ================================================================

print("\n\n========== SET QUESTION 6 ==========")

cities = {"Kolhapur", "Pune", "Mumbai", "Delhi", "Bengaluru"}

print("Cities:", cities)
print("Total number of cities:", len(cities))

array_module_methods()


# ================================================================
# SET QUESTION 7
# Display programming languages using a for loop.
# ================================================================

print("\n\n========== SET QUESTION 7 ==========")

languages = {"Python", "Java", "C", "C++", "JavaScript"}

for language in languages:
    print(language)

array_module_methods()


# ================================================================
# SET QUESTION 8
# Remove duplicate numbers using a set.
# ================================================================

print("\n\n========== SET QUESTION 8 ==========")

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = set(numbers)

print("Original list:", numbers)
print("List after removing duplicates:", list(unique_numbers))

array_module_methods()


# ================================================================
# SET QUESTION 9
# Find union of two sets.
# ================================================================

print("\n\n========== SET QUESTION 9 ==========")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)

print("Union:", union_set)

array_module_methods()


# ================================================================
# SET QUESTION 10
# Find common elements of two sets.
# ================================================================

print("\n\n========== SET QUESTION 10 ==========")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1.intersection(set2)

print("Common elements:", common)

array_module_methods()


# ================================================================
# SET QUESTION 11
# Find elements unique to each set.
# ================================================================

print("\n\n========== SET QUESTION 11 ==========")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

only_first = set1 - set2
only_second = set2 - set1

print("Only in first set:", only_first)
print("Only in second set:", only_second)

array_module_methods()


# ================================================================
# SET QUESTION 12
# Find elements present in either set but not both.
# ================================================================

print("\n\n========== SET QUESTION 12 ==========")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)

print("Elements in either set but not both:", result)

array_module_methods()


# ================================================================
# SET QUESTION 13
# Check whether first set is a subset of second.
# ================================================================

print("\n\n========== SET QUESTION 13 ==========")

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print("Is first set a subset?", set1.issubset(set2))

array_module_methods()


# ================================================================
# SET QUESTION 14
# Check whether first set is a superset of second.
# ================================================================

print("\n\n========== SET QUESTION 14 ==========")

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

print("Is first set a superset?", set1.issuperset(set2))

array_module_methods()


# ================================================================
# SET QUESTION 15
# Check whether two sets have no elements in common.
# ================================================================

print("\n\n========== SET QUESTION 15 ==========")

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print("Sets are disjoint:", set1.isdisjoint(set2))

array_module_methods()


# ================================================================
# SET QUESTION 16
# Check whether two sets are equal.
# ================================================================

print("\n\n========== SET QUESTION 16 ==========")

set1 = {1, 2, 3}
set2 = {3, 2, 1}

print("Are sets equal?", set1 == set2)

array_module_methods()


# ================================================================
# SET QUESTION 17
# Subjects studied by both students.
# ================================================================

print("\n\n========== SET QUESTION 17 ==========")

student1_subjects = {"Python", "Maths", "DBMS", "OS"}
student2_subjects = {"Java", "Maths", "DBMS", "CN"}

both_students = student1_subjects & student2_subjects

print("Subjects studied by both:", both_students)

array_module_methods()


# ================================================================
# SET QUESTION 18
# Accept a sentence and display unique words.
# ================================================================

print("\n\n========== SET QUESTION 18 ==========")

sentence = input("Enter a sentence: ")

words = set(sentence.lower().split())

print("Unique words:", words)

array_module_methods()


# ================================================================
# SET QUESTION 19
# Morning and afternoon session students.
# ================================================================

print("\n\n========== SET QUESTION 19 ==========")

morning = {"Amit", "Rahul", "Sneha", "Priya"}
afternoon = {"Sneha", "Priya", "Rohan", "Kiran"}

print("Present in both:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one session:", morning | afternoon)

array_module_methods()


# ================================================================
# SET QUESTION 20
# Students enrolled in Python and Java.
# ================================================================

print("\n\n========== SET QUESTION 20 ==========")

python_students = {"Amit", "Rahul", "Sneha", "Kiran"}
java_students = {"Priya", "Rahul", "Kiran", "Rohan"}

print("Python students:", python_students)
print("Java students:", java_students)

array_module_methods()


# ================================================================
# SET QUESTION 21
# Students enrolled in both courses and only one course.
# ================================================================

print("\n\n========== SET QUESTION 21 ==========")

python_students = {"Amit", "Rahul", "Sneha", "Kiran"}
java_students = {"Priya", "Rahul", "Kiran", "Rohan"}

print("Both courses:", python_students & java_students)
print("Only one course:", python_students ^ java_students)

array_module_methods()


# ================================================================
# SET QUESTION 22
# Technical skills of two employees.
# ================================================================

print("\n\n========== SET QUESTION 22 ==========")

employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "C++", "SQL", "Docker"}

print("Common skills:", employee1 & employee2)
print("Unique to Employee 1:", employee1 - employee2)
print("Unique to Employee 2:", employee2 - employee1)
print("All skills:", employee1 | employee2)

array_module_methods()


# ================================================================
# SET QUESTION 23
# Available books and requested books.
# ================================================================

print("\n\n========== SET QUESTION 23 ==========")

available_books = {
    "Python",
    "Java",
    "C++",
    "DBMS",
    "Operating System"
}

requested_books = {
    "Python",
    "DBMS",
    "Machine Learning"
}

print("Requested books that are available:",
      requested_books & available_books)

array_module_methods()


# ================================================================
# SET QUESTION 24
# Visitor IDs from two different days.
# ================================================================

print("\n\n========== SET QUESTION 24 ==========")

day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)

array_module_methods()


# ================================================================
# SET QUESTION 25
# Products belonging to different categories.
# ================================================================

print("\n\n========== SET QUESTION 25 ==========")

category1 = {"Laptop", "Mouse", "Keyboard", "Monitor"}
category2 = {"Monitor", "Printer", "Keyboard", "Scanner"}

print("Products in both categories:", category1 & category2)

array_module_methods()


# ================================================================
# SET QUESTION 26
# Friends of two users.
# ================================================================

print("\n\n========== SET QUESTION 26 ==========")

user1 = {"Amit", "Rahul", "Sneha", "Priya"}
user2 = {"Rahul", "Priya", "Rohan", "Kiran"}

print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", len(user1 | user2))

array_module_methods()


# ================================================================
#                    DICTIONARY QUESTIONS
# ================================================================


# ================================================================
# DICTIONARY QUESTION 1
# Student details.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 1 ==========")

student = {
    "roll_no": 101,
    "name": "Samarth",
    "department": "CSE",
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 2
# Employee information and specified key.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 2 ==========")

employee = {
    "id": 101,
    "name": "Rahul",
    "department": "IT",
    "salary": 60000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found.")

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 3
# Five products and prices. Add a new product.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 3 ==========")

products = {
    "Laptop": 60000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 9000
}

products["Webcam"] = 2500

print("Products:", products)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 4
# Update marks of a specified student.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 4 ==========")

marks = {
    "Amit": 80,
    "Rahul": 75,
    "Sneha": 90,
    "Priya": 85
}

student_name = input("Enter student name: ")

if student_name in marks:
    new_marks = int(input("Enter new marks: "))
    marks[student_name] = new_marks
    print("Updated dictionary:", marks)
else:
    print("Student not found.")

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 5
# Cities and populations. Remove a specified city.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 5 ==========")

population = {
    "Mumbai": 20000000,
    "Pune": 7000000,
    "Delhi": 30000000,
    "Bengaluru": 12000000
}

city = input("Enter city to remove: ")

if city in population:
    del population[city]
    print("Updated dictionary:", population)
else:
    print("City not found.")

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 6
# Employee IDs and names. Search employee ID.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 6 ==========")

employees = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha",
    104: "Priya"
}

employee_id = int(input("Enter employee ID: "))

if employee_id in employees:
    print("Employee exists:", employees[employee_id])
else:
    print("Employee ID does not exist.")

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 7
# Find number of key-value pairs.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 7 ==========")

records = {
    "Amit": 80,
    "Rahul": 75,
    "Sneha": 90,
    "Priya": 85
}

print("Total key-value pairs:", len(records))

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 8
# Display keys, values and key-value pairs.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 8 ==========")

data = {
    "Name": "Samarth",
    "Age": 20,
    "Department": "CSE"
}

print("Keys:", data.keys())
print("Values:", data.values())
print("Key-value pairs:", data.items())

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 9
# Programming languages and creators.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 9 ==========")

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup"
}

for language, creator in languages.items():
    print(language, ":", creator)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 10
# Accept five student names and marks.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 10 ==========")

student_marks = {}

for i in range(5):
    name = input("Enter student name: ")
    marks_value = float(input("Enter marks: "))
    student_marks[name] = marks_value

print("Student dictionary:", student_marks)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 11
# Find student with highest marks.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 11 ==========")

marks = {
    "Amit": 80,
    "Rahul": 95,
    "Sneha": 90,
    "Priya": 85
}

highest_student = max(marks, key=marks.get)

print("Highest marks:", highest_student)
print("Marks:", marks[highest_student])

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 12
# Find student with lowest marks.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 12 ==========")

marks = {
    "Amit": 80,
    "Rahul": 95,
    "Sneha": 70,
    "Priya": 85
}

lowest_student = min(marks, key=marks.get)

print("Lowest marks:", lowest_student)
print("Marks:", marks[lowest_student])

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 13
# Calculate average marks.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 13 ==========")

marks = {
    "Amit": 80,
    "Rahul": 95,
    "Sneha": 90,
    "Priya": 85
}

average = sum(marks.values()) / len(marks)

print("Average marks:", average)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 14
# Character frequency.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 14 ==========")

text = input("Enter a string: ")

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print("Character frequency:", frequency)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 15
# Word frequency in a sentence.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 15 ==========")

sentence = input("Enter a sentence: ")

word_frequency = {}

for word in sentence.lower().split():
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("Word frequency:", word_frequency)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 16
# Merge two dictionaries.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 16 ==========")

dict1 = {
    "a": 10,
    "b": 20
}

dict2 = {
    "c": 30,
    "d": 40
}

merged = {**dict1, **dict2}

print("Merged dictionary:", merged)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 17
# Find common keys.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 17 ==========")

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

print("Common keys:", common_keys)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 18
# Find common values.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 18 ==========")

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "x": 20,
    "y": 40,
    "z": 30
}

common_values = set(dict1.values()) & set(dict2.values())

print("Common values:", common_values)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 19
# Remove duplicate values while retaining first corresponding key.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 19 ==========")

data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

unique_values = {}

for key, value in data.items():
    if value not in unique_values.values():
        unique_values[key] = value

print("Dictionary after removing duplicate values:", unique_values)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 20
# Display dictionary in ascending order of keys.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 20 ==========")

data = {
    5: "E",
    2: "B",
    4: "D",
    1: "A",
    3: "C"
}

sorted_data = dict(sorted(data.items()))

print("Dictionary in ascending order:")
print(sorted_data)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 21
# Numbers 1 to 10 and their squares.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 21 ==========")

squares = {}

for number in range(1, 11):
    squares[number] = number ** 2

print("Squares:", squares)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 22
# Numbers 1 to 20, squares of even numbers only.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 22 ==========")

even_squares = {}

for number in range(1, 21):
    if number % 2 == 0:
        even_squares[number] = number ** 2

print("Even number squares:", even_squares)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 23
# Frequency of unique numbers in a list.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 23 ==========")

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print("Number frequency:", frequency)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 24
# Integers 1 to 10 and their cubes.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 24 ==========")

cubes = {}

for number in range(1, 11):
    cubes[number] = number ** 3

print("Cubes:", cubes)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 25
# Student management system.
# Add, update, delete, search, display, highest and average.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 25 ==========")

students = {
    "Amit": 80,
    "Rahul": 90,
    "Sneha": 85
}

# Add student
name = input("Enter student to add: ")
marks_value = float(input("Enter marks: "))
students[name] = marks_value

# Update marks
name = input("Enter student to update: ")

if name in students:
    students[name] = float(input("Enter new marks: "))
else:
    print("Student not found.")

# Delete student
name = input("Enter student to delete: ")

if name in students:
    del students[name]
else:
    print("Student not found.")

# Search student
name = input("Enter student to search: ")

if name in students:
    print("Student found. Marks:", students[name])
else:
    print("Student not found.")

# Display all students
print("All students:")

for name, marks_value in students.items():
    print(name, ":", marks_value)

# Highest marks
if students:
    highest = max(students.values())
    print("Highest marks:", highest)

# Average
if students:
    average = sum(students.values()) / len(students)
    print("Average marks:", average)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 26
# Employee salaries.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 26 ==========")

employees = {
    "Amit": 45000,
    "Rahul": 65000,
    "Sneha": 75000,
    "Priya": 50000,
    "Rohan": 80000
}

highest_salary = max(employees.values())
lowest_salary = min(employees.values())
average_salary = sum(employees.values()) / len(employees)

print("Highest salary:", highest_salary)
print("Lowest salary:", lowest_salary)
print("Average salary:", average_salary)

print("Employees earning more than Rs. 50,000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 27
# Product quantity management.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 27 ==========")

products = {
    "Laptop": 15,
    "Mouse": 8,
    "Keyboard": 20,
    "Monitor": 5
}

# Add product
product = input("Enter product to add: ")
quantity = int(input("Enter quantity: "))
products[product] = quantity

# Update quantity
product = input("Enter product to update: ")

if product in products:
    products[product] = int(input("Enter new quantity: "))
else:
    print("Product not found.")

# Delete product
product = input("Enter product to delete: ")

if product in products:
    del products[product]
else:
    print("Product not found.")

# Search product
product = input("Enter product to search: ")

if product in products:
    print("Product quantity:", products[product])
else:
    print("Product not found.")

# Products below 10
print("Products with quantity below 10:")

for product, quantity in products.items():
    if quantity < 10:
        print(product, ":", quantity)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 28
# Contact management system.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 28 ==========")

contacts = {
    "Amit": "9876543210",
    "Rahul": "9876501234"
}

# Add contact
name = input("Enter contact name to add: ")
phone = input("Enter phone number: ")
contacts[name] = phone

# Search contact
name = input("Enter contact to search: ")

if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found.")

# Update contact
name = input("Enter contact to update: ")

if name in contacts:
    contacts[name] = input("Enter new phone number: ")
else:
    print("Contact not found.")

# Delete contact
name = input("Enter contact to delete: ")

if name in contacts:
    del contacts[name]
else:
    print("Contact not found.")

# Display contacts
print("All contacts:")

for name, phone in contacts.items():
    print(name, ":", phone)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 29
# Book management system.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 29 ==========")

books = {
    101: "Python Programming",
    102: "Java Programming",
    103: "Data Structures"
}

# Add book
book_id = int(input("Enter book ID: "))
book_name = input("Enter book name: ")
books[book_id] = book_name

# Search book
book_id = int(input("Enter book ID to search: "))

if book_id in books:
    print("Book:", books[book_id])
else:
    print("Book not found.")

# Remove book
book_id = int(input("Enter book ID to remove: "))

if book_id in books:
    del books[book_id]
else:
    print("Book not found.")

# Display books
print("All books:")

for book_id, book_name in books.items():
    print(book_id, ":", book_name)

# Count books
print("Total books:", len(books))

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 30
# Group students according to department.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 30 ==========")

students = {
    "Amit": "CSE",
    "Rahul": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC",
    "Rohan": "IT",
    "Kiran": "CSE"
}

department_groups = {}

for student, department in students.items():

    if department not in department_groups:
        department_groups[department] = []

    department_groups[department].append(student)

print("Students grouped by department:")

for department, student_list in department_groups.items():
    print(department, ":", student_list)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 31
# Group words according to word length.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 31 ==========")

words = [
    "cat",
    "dog",
    "apple",
    "banana",
    "sun",
    "python",
    "car"
]

length_groups = {}

for word in words:

    length = len(word)

    if length not in length_groups:
        length_groups[length] = []

    length_groups[length].append(word)

print("Words grouped by length:")

for length, word_list in length_groups.items():
    print(length, ":", word_list)

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 32
# Find two numbers whose sum equals target.
# Uses a dictionary.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 32 ==========")

numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = {}

found = False

for number in numbers:

    required = target - number

    if required in seen:
        print(
            "Two numbers:",
            required,
            "and",
            number
        )
        found = True
        break

    seen[number] = True

if not found:
    print("No pair found.")

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 33
# Find first character that occurs only once.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 33 ==========")

text = input("Enter a string: ")

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

first_unique = None

for character in text:

    if frequency[character] == 1:
        first_unique = character
        break

if first_unique is not None:
    print("First non-repeating character:", first_unique)
else:
    print("No unique character found.")

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 34
# Find first character that occurs more than once.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 34 ==========")

text = input("Enter a string: ")

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

first_repeated = None

for character in text:

    if frequency[character] > 1:
        first_repeated = character
        break

if first_repeated is not None:
    print("First repeated character:", first_repeated)
else:
    print("No repeated character found.")

array_module_methods()


# ================================================================
# DICTIONARY QUESTION 35
# Accept paragraph.
# Key = word length
# Value = number of words having that length.
# ================================================================

print("\n\n========== DICTIONARY QUESTION 35 ==========")

paragraph = input("Enter a paragraph: ")

word_length_frequency = {}

words = paragraph.split()

for word in words:

    # Remove common punctuation marks
    word = word.strip(".,!?;:")

    length = len(word)

    word_length_frequency[length] = \
        word_length_frequency.get(length, 0) + 1

print("Word length frequency:")

for length, count in sorted(word_length_frequency.items()):
    print(
        "Word length:",
        length,
        "Number of words:",
        count
    )

array_module_methods()


# ================================================================
# END OF PROGRAM
# ================================================================

print("\n\n================================================")
print("ALL 60 QUESTIONS COMPLETED")
print("25 SET QUESTIONS + 35 DICTIONARY QUESTIONS")
print("ARRAY MODULE METHODS ALSO DEMONSTRATED")
print("================================================")