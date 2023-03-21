from unittests import square


def main():
    test_sqaure()

def test_sqaure():
    if square(2) != 4:
        print("2 sqaured was not 4")
    if square(3) != 9:
        print("3 sqaured was not 9")

if __name__ == "__main__":
    main()


# assert keyword
# Assert is a keyword in Python and some other languages as well
# that allow you to do exactly that, as in English, to assert
# that something is true, to sort of boldly claim that something is true.
# And if it is, nothing's going to happen.
# No errors are going to appear on the screen.
# But if you assert something in Python, and it is not true, that is,
# the thing you're insert asserting, a Boolean expression, is false,
# you're actually going to see some kind of error on the screen.
# assert shows where the error is. (not user friendly)
# let's use try and except (user friendly)
def main():
    test_sqaure()

def test_sqaure():
    try:
      assert square(2) == 4
    except AssertionError:
      print("2 sqaured was not 4")
    try:
      assert square(3) == 9
    except AssertionError:
       print("3 sqaured was not 9")
    try:
      assert square(-2) == 4
    except AssertionError:
       print("-2 sqaured was not 4")
    try:
      assert square(-3) == 9
    except AssertionError:
       print("-3 sqaured was not 9")
    try:
      assert square(0) == 0
    except AssertionError:
       print("0 sqaured was not 0")

if __name__ == "__main__":
    main()

# So pytest is a third party program that you can download and install
# that will automate the testing of your code, so long as you write the tests.
# But what's nice about this library and others
# like it is that it adopts some conventions so
# that you don't have to write as many lines of code yourself manually.
# They do some of that automatically for you.
# Now this is a third party library.
# There's other libraries for unit tests, so to speak,
# that is testing units of your code.
# Some of them come with Python itself.
# We're proposing that we look at pytest today
# because it's actually a little simpler than the unit
# testing frameworks that come with Python itself.
# And what do we mean by unit testing?
# Unit testing is just a formal way of describing testing
# individual units of your program.
# What are those individual units?
# They're typically functions.
# So unit tests are typically tests for functions that you have written.
# Now what does this mean in practice here.
# Let me go back to my VS code here and let
# me propose that we simplify my test calculator significantly.

def test_sqaure():
      assert square(2) == 4
      assert square(3) == 9
      assert square(-2) == 4
      assert square(-3) == 9
      assert square(0) == 0
  

# Per the documentation for pytest, which can itself be installed with pip
# install pytest, which we've used to install other libraries in the past,
# you can look at the documentation here for all of its formal usage.
# But fortunately, pytest is pretty user friendly, as testing frameworks go,
# and it actually allows us to dive right in by just running pytest on the code
# that we've written.
# pytest does show if there is an error but does not give the reason why.
# run pytest test_unittests.py in your terminal

def test_positive():
      assert square(2) == 4
      assert square(3) == 9

def test_negative():
      assert square(-2) == 4
      assert square(-3) == 9

def test_zero():
      assert square(0) == 0

