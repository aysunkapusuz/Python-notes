# Libraries are generally files of code that other people
# have written that you can use in your own programs or a library's code
# that you've written that you can use in your own program.
# This ability to share code with others, share code across your own projects.
# And it does so by way of what it calls module.
# A module in Python is just a library that typically has one or more functions or other features built into it.
# Generally, the purpose of a library or a module
# specifically is to encourage reusability of code.



# random modules
import random

coin = random.choice(["heads", "tails"])
print(coin)

# random.randint(a, b)
number = random.randint(1, 10)
print(number)

# random.shuffle()
cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)


# statistics 

import statistics

print(statistics.mean([100, 90]))
# the output will be 95

# command-line argument
# There's this feature generally known as command line arguments.
# This is a feature, not just of Python, but of languages
# more generally that allow you to provide input not when
# prompted inside of a program as happens whenever we call the Python function input.
# But rather, there's this feature, command line arguments of programs,
# that allows you to provide arguments that is input to the program of just when you're executing at the command line.
# So up until now, for instance, recall that we've generally
# run Python of something.py.
# For instance, Python of hello.py.
# And I've never once really executed any words or phrases
# after the name of the file, but we could.
# In fact, when you're running programs in a command-like environment like we are,
# you can provide any number of words or numbers or phrases after the command
# that you're typing.
# And all of those will somehow be passed in as inputs to the program itself.
# You don't have to prompt the user for one thing at a time
# by manually calling that input function.
# So what does this mean in real terms?

# sys, short for system, contains a whole lot of functionality
# that's specific to the system itself and the commands that you and I are typing.
# The documentation for this module is at this URL here.
# And it lists all of the various functions and variables and the like
# that come with that module.
# But we're going to focus on something a little more specific,
# namely this thing here.
# It turns out in the sys module in Python,
# there is a variable that just magically exists for you called argv.
# It stands for argument vector which is a fancy way of describing
# the list of all of the words that the human typed in at their prompt
# before they hit Enter.
# sys.argv
import sys

print("hello, my name is", sys.argv[1])


###
try: 
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

###
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])


# sys.exit()
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

###
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg)

# slices
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

    if len(sys.argv) < 2:
         sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)