# Define a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Accessing elements using positive indexing
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")

# Accessing elements using negative indexing
print(f"Last fruit: {fruits[-1]}")
print(f"Second last fruit: {fruits[-2]}")

# Accessing a range (slicing)
print(f"First three fruits: {fruits[:3]}")
print(f"Fruits from index 2 to end: {fruits[2:]}")
print(f"Middle fruits: {fruits[1:4]}")

# Modifying a list element
fruits[1] = "blueberry"
print(f"Modified list: {fruits}")

# Iterating through the list
print("All fruits in the list:")
for fruit in fruits:
    print(f"- {fruit}")
