# Conditionals unable us to ask questions and answer those questions, do you want to execute this line of code or other line of code.
# Built in syntax in Python 
# >
# >=
# <
# <=
# ==
# !=

# if keyword
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# elif keyword
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

#else keyword
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


# or 
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# let's make it better 
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# and
# another example
score = int(input("Score: "))


if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# increase the readability

value = int(input("Score: "))

if 90 <= value <= 100:
    print("Grade: A")
elif 80 <= value < 90:
    print("Grade: B")
elif 70 <= value < 80:
    print("Grade: C")
elif  60 <= value < 70:
    print("Grade: D")
else:
    print("Grade: F")

# even better
value = int(input("Score: "))

if value >= 90:
    print("Grade: A")
elif value >= 80:
    print("Grade: B")
elif value >= 70:
    print("Grade: C")
elif value >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# example 
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# bool (another data type) it can only True or False

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()



# better code
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False
    
main()

# even better
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0 
    
main()




name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# better
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# match keyword

name = input("What's your name? ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")