# Escape sequences
print("hello \"world\" world")
print('hello \'guys\' world')
print("I'm Harshit")
print("line a \nline b")  # New line sequence
print("Name \tHarshit")   # Tab sequence
print("this is backslash\\")   # \ is a backslash sequence

# Shortcut for comments: Use Ctrl + / (forward slash)

# Output: line a \n line b
print("line a \\n line b")
print("line a \\t line b")

# Output: \" \'
print("\\\"  \\'")

print("this is \\\\ double backslash")
print("these are /\\/\\/\\/\\ mountains")
print("I am \t awesome")
print(" \\\" \\n \\t \\' ")

# Raw string shortcut
print(r"line a \n line b")

# Printing an emoji
print("\U0001F602")

# Python as a calculator
print(2 + 3)  # Addition
print(8 - 6)  # Subtraction
print(3 * 3)  # Multiplication
print(4 / 2)  # Float division
print(2 // 4)  # Integer division
print(10 % 5)  # Modulus, gives remainder
print(2 ** 3)  # Exponentiation
print(round(2 ** 0.5, 4))  # Round off

# Variables
name = "harshit"
number1 = 5
print(number1)

# Snake case vs Camel case
user_one_name = "harshit"  # Snake case
userOneName = "gupta"  # Camel case

# Strings: Collection of characters inside quotes
first_name = "Harshit"
second_name = "Gupta"
full_name = first_name + " " + second_name  # Concatenation
print(full_name)
print(full_name + "3")  # No error
print(full_name + str(3))  # No error
print(full_name * 3)  # No error

# User input
name = input("What is your name: ")
print("Hello " + name)
age = input("What is your age? ")
print("Your age is " + age)

# int() function
number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
total = number_one + number_two
print("Sum is " + str(total))

# Multiple variable assignment
name, age = "Harshit", "20"
print(f"Hey mate {name}, and your age is {age}")

# Two inputs in one line
name, age = input("Enter name and age: ").split()
print(name)
print(age)

# String formatting
print(f"Hey {name}, your age is {age}")

# Average of three numbers using string formatting
num1, num2, num3 = map(int, input("Enter 3 numbers separated by commas: ").split(","))
print(f"The average is: {(num1 + num2 + num3) / 3}")

# String indexing
language = "python"
print(language[2])

# String slicing
print(language[0:6])
print(language[-3:6])

# String step argument
print("harshit"[::-1])  # Reverse string

# Reverse user input name
name = input("Enter your name: ")
print(f"Hey {name[::-1]}")

# String methods
name = "harshit gupta"
print(len(name))  # Length
print(name.lower())  # Lowercase
print(name.upper())  # Uppercase
print(name.title())  # Title case
print(name.count("a"))  # Count occurrences

# Exercise: Name length and character count (case insensitive)
name, char = input("Enter your name and a single character: ").split(",")
print(f"The length of your name is {len(name.strip())}")
print(f"Count of your character (case insensitive) is {name.strip().lower().count(char.strip().lower())}")

# Solving spaces in strings
name = "    harshit    "
dots = "..............."
print(name.strip() + dots)
print(name.replace(" ", "") + dots)

# Find and replace methods
string = 'she is beautiful and she is a good dancer'
print(string.replace(" ", "_"))
print(string.find("is", 1))

# Center method
name = "harshit"
print(name.center(11, "*"))
name = input("Enter your name: ")
print(name.center(len(name) + 8, "*"))

# Strings are immutable