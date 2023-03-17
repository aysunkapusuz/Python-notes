# Exceptions refer to problem in your code.
# print("hello, world) # syntax error
# You should solve syntax errors.



# value error
# if you answer this question as "dog" you will get an error. # invalid literal for int()
x = int(input("What's x? "))
print(f"x is {x}")

#try and except keywords
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")


# name error
# you do something with the name of variable but you should not
try:
    x = int(input("What's x? ")) # int function is not working here
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

# else keyword
# else solves the problem
try:
    x = int(input("What's x? ")) 
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")