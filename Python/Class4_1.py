# Assign the string "Hello" to the variable 'var'
var = "Hello"

# Convert the string to uppercase letters
var.upper()  # Output: 'HELLO'

# Convert the string to lowercase letters
var.lower()  # Output: 'hello'

# Get a substring of 'var' from index 0 to 3 (4 is excluded)
var[0:4]  # Output: 'Hell'

# Check if the string starts with "H"
var.startswith("H")  # Output: True

# Check if the string starts with "M"
var.startswith("M")  # Output: False

# Convert the string to lowercase and check if it starts with "h"
var.lower().startswith("h")  # Output: True

# Convert the string to lowercase and check if it starts with "H"
var.lower().startswith("H")  # Output: False

# Check if the string ends with "d"
var.endswith("d")  # Output: False

# Check if the string ends with "o"
var.endswith("o")  # Output: True

# Assign a new string with dots to 'var'
var = "Hello.World.Devops"

# Split the string into a list at each dot (".")
var.split(".")  # Output: ['Hello', 'World', 'Devops']

# Assign a new string with pipes ("|") to 'var'
var = "Hello|World|Devops"

# Split the string into a list at each pipe ("|")
var.split("|")  # Output: ['Hello', 'World', 'Devops']

# Split the string into separate variables
var1, var2, var3 = var.split("|")

# Print the first part of the split
print(var1)  # Output: 'Hello'

# Print the second part of the split
print(var2)  # Output: 'World'

# Print the third part of the split
print(var3)  # Output: 'Devops'

# Check the type of 'var1'
type(var1)  # Output: <class 'str'>

# Split the string into at most 2 parts at the pipe ("|")
var.split("|", 2)  # Output: ['Hello', 'World', 'Devops']

# Split the string into at most 1 part at the pipe ("|")
var.split("|", 1)  # Output: ['Hello', 'World|Devops']

# Assign a new string with dots to 'var'
var = "hello.wrold.new"

# Split the string into at most 2 parts at the dot (".")
var.split(".", 2)  # Output: ['hello', 'wrold', 'new']

# Split the string into at most 1 part at the dot (".")
var.split(".", 1)  # Output: ['hello', 'wrold.new']

# Assign another string with dots to 'var'
var = "a.b.c.d.e"

# Split the string into a list at each dot
var.rsplit(".")  # Output: ['a', 'b', 'c', 'd', 'e']

# Split the string into at most 2 parts, starting from the right
var.rsplit(".", 2)  # Output: ['a.b.c', 'd', 'e']

# Create a range of numbers from 1 to 99 (100 is excluded)
range(1, 100)  # Output: range(1, 100)
