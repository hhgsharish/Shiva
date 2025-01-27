# Import the sys module for system-specific functions
import sys
# Import the random module to generate random numbers
import random
# Import the os module to interact with the operating system
import os

# Print a random number between 1 and 100
print(random.randint(1, 100))

# Loop through numbers 1 to 4 and print each number
for i in range(1, 5):
    print(i)

# Print the name of the script being executed (argv[0] is the script name)
print(sys.argv[0])

# Change the current working directory to /home/harish
os.chdir("/home/harish")

# Create a new directory named "new_directory1" inside the current directory
# If the directory already exists, no error will be raised (exist_ok=True)
os.makedirs("new_directory1", exist_ok=True)

# List all files and directories in /home/harish and print them
print(os.listdir("/home/harish"))

# Print the current working directory (after changing to /home/harish)
print(os.getcwd())

# Walk through the directory tree starting at /home/harish/new_directory
# For each directory, print the path, subdirectories, and files
for path, dirs, files in os.walk("/home/harish/new_directory"):
    print(path, dirs, files)
