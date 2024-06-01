# Create a list with the numbers from 1 to 10
numbers = list(range(1, 11))
print(numbers)

# Use a for loop to print each number in the list
for number in numbers:
    print(number)

# Create a list 1-10 and for loop to print only even numbers
numbers = list(range(1, 11))

for number in numbers:
    if number % 2 == 0:
        print(number)

# Create a list 1-10 and for loop to print only odd numbers
numbers = list(range(1, 11))

for number in numbers:
    if number % 2 != 0:
        print(number)

# Create a list of 5 names then for loop to print each name on list
names = ["Anna", "Bob", "Charlie", "Darleen", "Emely"]
for name in names:
    print(name)

# Create a list of 5 names then for loop and only print names that start with a
names = ["Anna", "Bob", "Anne-Bob", "Darleen", "Emely"]
for name in names:
    if name.startswith("A"):
        print(name)

# Create list of 5 names and only print if name has more than 5 characters
names = ["Anna", "Bob", "Anne-Bob", "Darleen", "Emely"]
for name in names:
    if len(name) > 5:
        print(name)

# Create list of 5 names use for loop to print list in uppercase
names = ["Anna", "Bob", "Anne-Bob", "Darleen", "Emely"]
for name in names:
        print(name.upper())

# Use a for loop and range function to print Hello 100x
for _ in range(100):
    print("Hello")

# Using a for loop and range function print numbers from 1-100
for number in range(1, 101):
    print(number)



