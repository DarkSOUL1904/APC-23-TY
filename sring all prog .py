#•	Write a program to input a string and display its length without using the len() function. 
s = input("Enter a string: ")

count = 0
for ch in s:
    count += 1

print("Length of the string is:", count)

#•	Count the number of vowels, consonants, digits, spaces, and special characters in a given string
s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)


#	Reverse the given string without using built-in reverse functions
s = input("Enter a string: ")

reversed_string = ""

for ch in s:
    reversed_string = ch + reversed_string


print("Reversed string:", reversed_string)

#•	Check whether the entered string is a palindrome. 

s = input("Enter a string: ")

rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#•	Count the number of uppercase and lowercase letters in a string. 
s = input("Enter a string: ")

uppercase = 0
lowercase = 0

for ch in s:
    if 'A' <= ch <= 'Z':
        uppercase += 1
    elif 'a' <= ch <= 'z':
        lowercase += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)

#•	Replace all occurrences of a given character with another character. 

s = input("Enter a string: ")

old_char = input("Enter the character to replace: ")

new_char = input("Enter the new character: ")

result = ""

for ch in s:
    if ch == old_char:
        result += new_char
    else:
        result += ch

print("Modified string:", result)

#•	Remove all spaces from the input string. 
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print("String after removing spaces:", result)

#•	Find the number of times a specified character appears in a string. 
text = input("Enter a string: ")
char = input("Enter a character: ")

count = text.count(char)

print("Occurrences:", count)

#•	Print the first and last character of a string. 
text = input("Enter a string: ")

print("First character:", text[0])
print("Last character:", text[-1])

#•	Display each character of a string along with its ASCII value.
text = input("Enter a string: ")

for ch in text:
    print(ch, ord(ch))
    
# Count the total number of words in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Word count:", len(words))

# Find the longest word in a given sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Longest word:", max(words, key=len))

# Find the shortest word in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Shortest word:", min(words, key=len))

# Convert the first letter of every word to uppercase.

text = input("Enter a string: ")
print(text.title())

# Print all duplicate characters in a string.

text = input("Enter a string: ")
seen = set()
duplicates = set()

for ch in text:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)

print("Duplicate characters:", *duplicates)

# Display the frequency of every character in a string.

text = input("Enter a string: ")

for ch in set(text):
    print(ch, ":", text.count(ch))

    
    
# Check whether two strings are anagrams.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower()):
    print("Anagram")
else:
    print("Not Anagram")

# Remove duplicate characters while maintaining the original order.

text = input("Enter a string: ")
result = ""

for ch in text:
    if ch not in result:
        result += ch

print(result)

# Check whether a given substring exists in the main string.

main = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in main:
    print("Substring found")
else:
    print("Substring not found")

# Count how many times a specific word appears in a sentence.

sentence = input("Enter a sentence: ")
word = input("Enter word to count: ")

print("Occurrences:", sentence.split().count(word))

# Validate a password based on given conditions.

password = input("Enter password: ")

if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password) and
    any(c.isdigit() for c in password) and
    any(not c.isalnum() for c in password)):
    print("Valid Password")
else:
    print("Invalid Password")

# Compress a string by counting consecutive repeated characters.

text = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        result += text[i - 1] + str(count)
        count = 1

result += text[-1] + str(count)

print(result)

# Compress repeated characters and return original string if compression is not shorter.

text = input("Enter a string: ")

compressed = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        compressed += text[i - 1] + str(count)
        count = 1

compressed += text[-1] + str(count)

if len(compressed) < len(text):
    print(compressed)
else:
    print(text)

# Find the character with the highest frequency.

text = input("Enter a string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(max(freq, key=freq.get))

# Find the second most frequently occurring character.

text = input("Enter a string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(sorted_chars) > 1:
    print(sorted_chars[1][0])
else:
    print("No second frequent character")

# Encrypt and decrypt a message using the Caesar Cipher algorithm.

text = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        encrypted += chr((ord(ch) - base + shift) % 26 + base)
    else:
        encrypted += ch

print("Encrypted:", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        decrypted += chr((ord(ch) - base - shift) % 26 + base)
    else:
        decrypted += ch

print("Decrypted:", decrypted)

# Validate whether a given email address follows a valid format.

email = input("Enter email: ")

if "@" in email and "." in email.split("@")[-1]:
    print("Valid Email")
else:
    print("Invalid Email")

# Count the frequency of every word in a paragraph.

text = input("Enter paragraph: ")

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

# Reverse the order of words in a sentence without changing the words themselves.

sentence = input("Enter a sentence: ")

words = sentence.split()
print(" ".join(words[::-1]))

# Check whether one string is a rotation of another.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes")
else:
    print("No")