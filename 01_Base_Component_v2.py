import random

# Functions go here -
def yes_no (question):
  valid = False
  while not valid:
    response =  input(question).lower()

    if response == "yes" or response == "y":
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

# Number checking function goes here
print()
def int_check(question, low=None, high=None):

  situation = ""

  if low is not None and high is not None:
    situation = "both"
  elif low is not None and high is None:
    situation = "low only"

  while True:

    try:
      response = int(input(question))

      # checks input is not too high or
      #too low if a both upper and lower bounds
      # are specified
      if situation == "both":
        if response < low or response > high:
          print("Please enter a number between"
               "{} and {}".format(low, high))
          continue

      # checks input is not too low
      elif situation == "low only":
        if response < low:
          print("Please enter a number that is more"
               "than (or equal to) {}".format(low))
          continue

      return response

    #checks input is a integer
    except ValueError:
      print("Please enter an integer")
      continue

      
# Main routine

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)