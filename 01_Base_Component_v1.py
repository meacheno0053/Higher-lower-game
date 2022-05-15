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
        
**** INSTRUCTIONS ****
  
""")
  return""

# main routine starts here
played_before = yes_no("have you played before?")

if played_before == "no":
  instructions()