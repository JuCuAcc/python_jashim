
# The with statement makes sure the file is closed properly when
#   the program has finished accessing the file.

filename = 'D:\\Python Practice\\python_jashim\\python_basic\\files\\jashim.txt'

with open(filename) as f_obj:
    contents = f_obj.read()

print(contents)

# Reading line by line
# The rstrip() method gets rid of the extra blank lines
#   this would result in when printing to the terminal.

filename = 'D:\\Python Practice\\python_jashim\\python_basic\\files\\jashim.txt'

with open(filename) as f_obj:
   for line in f_obj:   
    print(line.rstrip())


# Storing the lines in a list

filename = 'D:\\Python Practice\\python_jashim\\python_basic\\files\\jashim.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:   
    print(line.rstrip())

print("==============================")
print("==============================")

# Writing to a file
# 'w' = erase contents
# 'a' = append contents

filename = 'D:\\Python Practice\\python_jashim\\python_basic\\files\\jashim.txt'

with open(filename , 'w') as f:
    f.write("I love programming!\n")
    f.write("I love creating new games.\n")

with open(filename , 'a') as f:
    f.write("I also working with data.\n")
    f.write("I love making apps as well.\n")

with open(filename) as f:
    contents = f.read()
print(contents)

# File paths
# When Python runs the open() function, it looks for the file in 
# the same directory where the program that's being executed is stored.
# You can open a file from a subfolder using a relative path.
# You can also use an absolute path to open any file on your system.

# Openinf a file from a subfolder
f_path = "text_files/uddin.txt"

with open(f_path) as f_obj: 
    lines = f_obj.readlines()

for line in lines: 
    print(line.rstrip())

# Opening a file using an absolute path
f_path = "D:/Python Practice/python_jashim/python_files/text_files/uddin.txt"

with open(f_path) as f_obj: 
    lines = f_obj.readlines()

for line in lines: 
    print(line.rstrip())

# Opening a file using relative path
f_path = "../python_basic/files/jashim.txt"

with open(f_path) as f_obj: 
    lines = f_obj.readlines()

for line in lines: 
    print(line.rstrip())

print("==============================")
print("==============================")

# try-except

# Handling the ZeroDivisionError exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Handling the FileNotFound exception
f_name = '../python_basic/files/jashim.txt'

try:
    with open(f_name) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    msg = "Can't find file {0}.".format(f_name)
    print(msg)

# Try writing your code without a try block, and make it gnerate an error.
# The traceback will tell you what kind of exception your program needs to handle.

# Using an else block
# Any code depends on the try block running successfully should be placed in the else block.

print("Enter two numbers. I'll divide them.")

x = input("First number: ")
y = input("Second number: ")

try:
    result = int(x) / int(y)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(result)

## Preventing crashes from user input

#"""A simple calculator for division only."""

#print("Enter two numbers. I'll divide them.")
#print("Enter 'q' to quit.")

#while True: 
#    x = input("\nFirst number: ")
#    if x == 'q':
#        break
#    y = input("Second number: ")
#    if y == 'q':
#        break
#    try:
#        result = int(x) / int(y)
#    except ZeroDivisionError:
#        print("You can't divide by zero!")
#    else:
#        print(result)

# Using the pass statement in an else block allows you to just continue running the program.
f_names = ['jashim.txt', 'uddin.txt', 'moby_dick.txt', 'little_women.txt']

for f_name in f_names: 
    # Report the length of each file found.
    try:
        with open(f_name) as f_obj: 
            lines = f_obj.readlines()
    except FileNotFoundError:
        # Just move on to the next file.
        pass
    else:
        num_lines = len(lines)
        msg = "{0} has {1} lines.".format(f_name, num_lines)
        print(msg)

# Don't use bare except blocks
try:
    # Do something
    pass
except:
    pass

# Use Exception instead
try:
    # Do something
    pass
except Exception:
    pass

# Printing the Exception 
try:
    # Do something
    pass
except Exception as e:
    print(e, type(e))



# Storing data with json
# Using json.dump() to store data

"""Store some numbers"""

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'text_files/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)


# Making sure the stored data exists
import json

filename = 'text_files/numbers.json'

try:
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
except FileNotFoundError:
    msg = "Can't find {0}.".format(f_name) 
    print(msg)
else:
    print(numbers)