name = input("What's your name? ")
print(f"hello, {name}")

#####
names = []

for _ in range(3):
    names.append(input("What's your name? "))

######
# sort it
for name in sorted(names):
    print(f"hello, {name}")

# all the names are lost when you restart the program
# And that's where File I/O comes in.
# And that's where files come in.
# They are a way of storing information persistently on your own phone, or Mac,
# or PC, or some cloud server's disk so that they're there when you
# come back and run the program again.

# here is how we can solve the problem
# So open is like the programmer's equivalent of double clicking
# on an icon on your Mac or PC.
# But it's a programmer's technique because it's
# going to allow you to specify exactly what you want
# to read from or write to that file.


name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# with 
# You say, with, you call the function in question,
# and then you say as and specify the name of the variable that should
# be assigned the return value of open.
# Then I'm going to go ahead and indent the line underneath so
# that the line of code that's writing the name
# is now in the context of this with statement, which just ensures that,
# automatically, if I had more code in this file
# down below no longer indented, the file would be automatically closed
# as soon as line 4 is done executing.

name = input("What's your name? ")

with open("names.txt", "a") as file:
     file.write(f"{name}\n")


# But I'm going to keep reusing the same name just to keep us focused on this.
# And now I'm going to write code that reads an existing file with Hermione,
# Harry, Ron, and Draco together.
# And how do I do this?
# Well, it's similar in spirit.
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

####
with open("names.txt", "r") as file:
       for line in file:
           print("hello,", line.rstrip())
 
 # sort the output
names = []

with open("names.txt") as file:
       for line in file:
           names.append(line.rstrip())

for name in sorted(names):
           print(f"hello, {name}")

# make it better
with open("names.txt") as file:
       for line in sorted(file):
           print("hello,", line.rstrip())


# reverse
names = []

with open("names.txt") as file:
       for line in file:
           names.append(line.rstrip())

for name in sorted(names, reverse=True):
           print(f"hello, {name}")


# csv stands for Comma-Separated Values.
# And it's a very common convention to store multiple pieces of information
# that are related in the same file.

# And it turns out, these CSV files are very commonly
# used when you use something like Microsoft Excel, Apple Numbers,
# or Google Spreadsheets, and you want to export the data to share
# with someone else as a CSV file.
# Or conversely, if you want to import a CSV
# file into your preferred spreadsheet software,
# like Excel, or Numbers, or Google Spreadsheets, you can do that as well.
# So CSV is a very common, very simple text format
# that just separates values with commas and different types of values,
# ultimately, with new lines as well.

with open("students.csv") as file:
      for line in file:
            name, house = line.rstrip().split(",")
            print(f"{name[0]} is in {house[1]}")


# sort it
students = [] 

with open("students.csv") as file:
      for line in file:
            name, house = line.rstrip().split(",")
            students.append(f"{name} is in {house}")

for student in sorted(students):
      print(student)

#####
students = [] 

with open("students.csv") as file:
      for line in file:
            name, house = line.rstrip().split(",")
            student = {}
            student["name"] = name
            student["house"] = house
            students.append(student)

for student in students:
      print(f"{student['name']} is in {student['house']}") # why do we use single quotes here?
# Because I'm already using double quotes outside of the f string, if I want to put quotes
# around any strings on the inside, which I do need to do for dictionaries because, recall, when you index
# into a dictionary, you don't use numbers like lists--
# 0, 1, 2, onward--
# you, instead, use strings, which need to be quoted.
# But if you're already using double quotes,
# it's easiest to then use single quotes on the inside,
# so Python doesn't get confused about what lines up with what.

students = [] 

with open("students.csv") as file:
      for line in file:
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house}
            students.append(student)

def get_name(student):
      return student["name"]

for student in sorted(students, key=get_name):
      print(f"{student['name']} is in {student['house']}")


# we can get rid of the function get_name
# lambda is a another keyword
students = [] 

with open("students.csv") as file:
      for line in file:
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house}
            students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
      print(f"{student['name']} is in {student['house']}")


# csv.reader() from csv module
# import csv
students = [] 

with open("students.csv") as file:
      reader = csv.reader(file)
      for name, home in reader: 
            students.appends({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
      print(f"{student['name']} is in {student['house']}")

# DictReader()
students = [] 

with open("students.csv") as file:
      reader = csv.DictReader(file)
      for name, home in reader: 
            students.appends({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
      print(f"{student['name']} is in {student['house']}")

###
import csv

name = input("What's your name? ")
home = input("What's your home? ")

#a is append mode
with open("students.csv", "a") as file:
      writer = csv.writer(file)
      writer.writerow([name, home])


### 
with open("students.csv", "a") as file:
      writer = csv.DictWriter(file, fieldnames=["name", "home"])
      writer.writerow({"name" : name, "home": home})

# You can store data any way that you want.
# We've just picked CSVs because it's representative
# of how you might read and write from a file
# and do so in a structured way, where you can somehow have multiple keys,
# multiple values all in the same file without having to resort to what would
# be otherwise known as a binary file.
# So a binary file is a file that's just zeros and ones.
# And they can be laid out in any pattern you might want, particularly
# if you want to store not textual information,
# but maybe graphical, or audio, or video information as well.
# So it turns out that Python is really good
# when it comes to having libraries for, really, everything.
# And in fact, there's a popular library called
# pillow that allows you to navigate image files as well
# and to perform operations on image files.