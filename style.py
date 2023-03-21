# Style is rather subjective, and it depends typically on the programmer, on the company,
# that you're actually using.
# But within the Python community, it turns out
# that there's some pretty regimented standards
# that most all python Programmers adhere to,
# or rather, are expected to adhere to, because this particular language
# and community has tried to codify some of their preferences
# for how your code should look in the form of something called PEP 8.

# Python enhancement proposal-- is a set of proposals
# that the community within the world of Python
# typically generate to not only propose new ideas, but also to codify,
# ultimately, certain standards.
# And PEP 8 happens to be such a proposal that standardized, or rather tried
# to standardize, what our code should look like-- that is to say,
# it's quite possible to write code that's not only correct,
# it might even be well designed, but it's just really a mess.
# And it just doesn't look very good.
# It's therefore harder to read.
# It's harder for others to read.
# And therefore, it's just not as maintainable.
# And any time you make something harder to read or less maintainable,
# you're just increasing the probability, dare say down
# the line, of introducing bugs.
# So it's a good thing for your code to be properly formatted,
# just like in the world of writing emails or essays or books or documents
# or beyond.

# it turns out that it tries to standardize
# a number of details that would be manifest in your own code
# once you've written a number of lines.
# And the overarching premise of PEP 8, and really
# the notion of style in the Python community especially,
# is that "readability counts."
# And typically, languages-- Python among them--
# come with what's generally known as a style guide.
# A style guide, not unlike PEP 8, is some kind
# of guide-- a document, either printed or perhaps internet
# based-- that just tries to standardize what everyone's code should look like.

# Indentation
# Tabs ans Spaces?
# Maximum Line Length
# Blank Lines
# Imports

# pip install pylint
# And one of the most popular in the world of Python
# is a program called pylint, which is an example of what's
# generally known as a linter, which is a program that rather statically
# analyzes.
# That is-- reads your code top to bottom, left to right,
# and tries to figure out if there are potentially mistakes therein,
# or at least inconsistencies with something like a prescribed style
# guide.
# But it turns out there's other tools out there as well that are perhaps
# a little less noisy than pylint.
# It turns out if you run pylint on most of the programs
# you've written thus far, odds are you're going
# to be overwhelmed with just how many things you apparently did wrong
# stylistically, even though your code may very well be both correct
# and well designed.

# pip install black
# And indeed, that's the spirit of this particular formatter called black,
# which is that it's opinionated, more so than others.
# With a lot of these formatters that exist out there, you tend to--
# or your company tends to, or your course tends
# to configure them with certain rules.