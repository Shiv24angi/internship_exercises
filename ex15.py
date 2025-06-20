from sys import argv

script, filename = argv

# Open the file
txt = open(filename)

# Print filename using %r (repr-style string)
print("Here's your file %r:" % filename)
print(txt.read())

# Ask the user to enter the filename again
print("Type the filename again:")
file_again = input("> ")

# Open and read the file again
txt_again = open(file_again)

print(txt_again.read())
