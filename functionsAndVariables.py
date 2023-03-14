# let's write our first code
# use terminal, write a command python functionsAndVariables.py or use code runner extention
print("Hello, world.")

# FUNCTIONS
# Functions let you do something in the program. 
# Argument is an input to a function that influence it's behavior.

# input function let user's take action to answer questions
input("What's your name? ")
print("Hello, world.")

# Variables can store a value
name = input("What's your name? ")
print("Hello, world.")

#say hello to user
print("hello, " + name)
print("hello,", name)

#str stands for string (one of the data types)
# https://docs.python.org/3/library/stdtypes.html#string-methods (take a look)
# https://docs.python.org/3/library/functions.html

#end and sep they are parameters 
print("hello, ", end="")
print(name)

print("hello,", name, sep="")

#you can use f {} for variables
print(f"hello, {name}")

# strip() method removes whitespace from str and capitalize() capitalize first letter of the given input
surname = input("What's your surname? ")
surname = surname.strip().capitalize()
surname = surname.title() #title is better if let's say you two inputs,, Mike John
print(f"Hello, {surname}")

#more clean an readbale
surname = input("What's your surname? ").strip().title() 
print(f"Hello, {surname}")

#split(" ") method
first, last = surname.split(" ")
print(f"hello, {first}")



# int stands for integer (another data type)
# + - * / % 

x = 1
y = 2
z = x + y
print(z)

# This is not gonna work. the result will be string
x = input("What's x? ")
y = input("What's y? ")
z = x + y
print(z)

# Now, that works.
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

# float(), decimal point (another data type)

x = float(input("What's x? "))
y = float(input("What's y? "))
print(x + y)
# 1.2 + 2.3 = 3.5
# http://docs.python.org/3/library/functions.htmI#round (take a look)

x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
a = round(x / y, 2)
print(a)
print(z)
print(f"{z:,}")

# You can invent your own function by using def keyword stands for define

def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)


def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)



def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)



def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n**2

main()



