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



while True:
          try:
              x = int(input("What's x? ")) 
          except ValueError:
              print("x is not an integer")
          else:
              break
          
print(f"x is {x}")




def main():
     x = get_int()
     print(f"x is {x}")

def get_int():    
    while True:
              try:
                  x = int(input("What's x? ")) 
              except ValueError:
                  print("x is not an integer")
              else:
                  break
              return x

main()





def main():
     x = get_int()
     print(f"x is {x}")

def get_int():    
    while True:
              try:
                  return int(input("What's x? ")) 
              except ValueError:
                  print("x is not an integer")

main()

# pass  # silently ignoring 

def main():
     x = get_int()
     print(f"x is {x}")

def get_int():    
    while True:
              try:
                  return int(input("What's x? ")) 
              except ValueError:
                  pass

main()



def main():
     x = get_int("What's x? ")
     print(f"x is {x}")

def get_int(prompt):    
    while True:
              try:
                  return int(input(prompt)) 
              except ValueError:
                  pass

main()


# raise keyword





