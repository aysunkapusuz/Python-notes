# Looping means repeating something over and over until a particular condition is satisfied.
# while loop allow us to ask question again and again

i = 3
while i != 0:
    print("meow")
    i = i - 1
# the executed code is:
#meow
#meow
#meow

i = 0
while i < 3:
    print("meow")
    i = i + 1 # = is not equal sign. it assignes the value from left to right.

i = 0
while i < 3:
    print("meow")
    i += 1 # another syntax

# for loop. Iterate over a list of items
# list another data type / list of things
for i in [0, 1, 2]:
    print("meow")

# range()
for i in range(15):
    print("meow")

#minor improvement 
for _ in range(15): # if you are really not using the variable you can use _ sign
    print("meow")


print("meow" * 3)
# it will print meowmeowmeow

print("meow\n" * 3, end="")
# now it will print:
#meow
#meow
#meow


while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")



# let's create a meow function
# it will print meow 3 times
def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()

#let's ask user to get value
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
        return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

#using list
students = ["Marry", "Harry", "John"]
print(students[0])
print(students[1])
print(students[2])

#you can use for loop to iterate anything
students = ["Marry", "Harry", "John"]

for student in students:
    print(student)

# len will tell you the length of a list
students = ["Marry", "Harry", "John"]

for i in range(len(students)):
    print(students[i])

    students = ["Marry", "Harry", "John"]

for i in range(len(students)):
    print(i + 1, students[i])

# dict is a data structure that allows you to associate one value with another

students = {
    "Marry": "A", 
    "Harry": "B", 
    "John": "C"
    }

print(students["Marry"]) #A
print(students["Harry"]) #B
print(students["John"]) #C


# we will only see students
students = {
    "Marry": "A", 
    "Harry": "B", 
    "John": "C"
    }

for student in students:
    print(student)
# Marry
# Harry
# John


students = {
    "Marry": "A", 
    "Harry": "B", 
    "John": "C"
    }

for student in students:
    print(student, students[student], sep=", ")

# Marry, A
# Harry, B
# John, C


# None keyword / this means absent of a value
students = [
    {"name": "Marry", "house": "A", "favcolor": "green"},
    {"name": "Harry", "house": "B", "favcolor": "black"},
    {"name": "John", "house": "C", "favcolor": "yellow"},
    {"name": "Jen", "house": "D", "favcolor": None}
]

for student in students:
    print(student["name"], student["house"], student["favcolor"], sep=", ")

# Marry, A, green
# Harry, B, black
# John, C, yellow
# Jen, D, None



def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")


main()
# #
# #
# #

def main():
    print_column(3)

def print_column(height):
        print("#\n" * height, end="")

main()
# #
# #
# #




def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
# ????


def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
        # Print brick
            print("#", end="")
        print()
main()
# ###
# ###
# ###



def main():
    print_square(3)

def print_square(size):
    for i in range(size):
            print("#" * size)

main()
# ###
# ###
# ###



def main():
    print_square(3)

def print_square(size):
    for i in range(size):
            print("#" * size)

main()

