import random

# Functions go here -
def yes_no (question):
  valid = False
  while not valid:
    response =  input(question).lower()

    if response == "yes" or response == "y":
      print("you chose yes")
      return "yes"

    elif response == "no" or response == "n":
      return "no"

    else:
      print("please answer yes / no")


def instructions ():
  print()
  print("**** How to play ****")
  print()
  print("""
        
---- INSTRUCTIONS ----
  
""")
  return""

# decoration
def statement_generator(statement, decoration, style):

  sides = decoration * 3

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  if style == 3:

    print(top_bottom)
    print(statement)
    print(top_bottom)
  else:
    print(statement)

  return ""

# main routine starts here
statement_generator("** welcome to the higher lower game **", "*", 3)
print()
played_before = yes_no("have you played before?")

if played_before == "no":
  instructions()