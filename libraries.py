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



# Python comes with to talk about more generally packages that exist.
# One of the reasons that Python is so popular and powerful these days
# is that there's a lot of third-party libraries
# out there as well, otherwise known as packages.
# Python itself has a term of art called a package, which is a module essentially
# that's implemented in a folder, not just a file but a folder.
# But more generally, a package is a third-party library that you,
# that I can install on our own Mac or PC or our cloud server
# and gain access to even more functionality that other people have implemented for us.
# Now, one of the locations you can get all of these packages
# is called the PYTI website, the Python Package Index which lives at this URL
# here.
# And this is a website that is searchable via the command line,
# as well as via the web, that allows you to download and install
# all sorts of packages.
# Now, there's a fun one out there that's a throwback to a command that's
# been around for years in command line environments called cowsay.
# Cowsay is a package in Python that allows you to have a cow say something
# on your screen.

# Nowadays, a lot of languages, Python among them, has what's called its own package manager.
# This one called pip which is just one.
# Pip is a program that generally comes with Python itself, nowadays,
# that allows you to install packages onto your own Macs or PCs or cloud environment by just running a command.
# And then, you have access to a whole new library in Python
# that didn't come with Python itself.
# But now it's available on your system for you.

# APIs
# An API is an application programming interface.
# And it can refer to Python files and functions.
# But often, APIs really refer to third-party services
# that you and I can write code that talk to.
# Many APIs, but not all, live on the internet these days so that so long as you have a browser or so long
# as you have some experience with Python programming or programming
# in any language, you can write code that in effect pretends to be a browser,
# connects to that third-party API on a server,
# and download some data that you can then incorporate into your own program.
# Now, how do you do this?
# Python has a very popular package that you
# can install via pip called requests.
# The requests library allows you to make web request,
# internet request using Python code essentially
# as though you were a browser yourself.
# You can automate, therefore, the retrieval of URLs
# that start with HTTP or HTTPS.
# The documentation for this library is that a URL like this,
# but it too can be installed at the command line.
# And even though it's third party, it's one
# of the most popular and commonly used packages out there in Python.


# There is a standard text format known as JSON--
# JavaScript Object Notation is technically related to yet,
# another programming language called JavaScript.
# But JSON itself is typically used nowadays
# as a language agnostic format for exchanging data between computers.
# By language agnostic, that means you don't have to use JavaScript.
# We can use Python or any other language to read JSON or write it as well.
# And it's a completely text-based format, which
# means that if I visit that URL with my browser, what gets downloaded
# is just a bunch of text.