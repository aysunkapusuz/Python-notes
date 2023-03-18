def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)

if __name__ == "__main__":
    main()

# if height is 3 the result will be:
#
# #
# ##

# and this is not what we really want 


def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print(i, end=" ") # we can use print for debugging
        print("#" * i)

if __name__ == "__main__":


    main()
# and thw new result will be:
# 0
# 1 #
# 2 ##

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i + 1)) # here is the solution

if __name__ == "__main__":
    main()

# new result is:
# #
# ##
# ###

# we can also use breakpoints for debugging