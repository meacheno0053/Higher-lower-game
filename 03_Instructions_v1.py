
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
  print("**** How to play ****")
  print(""" 
        
***** INSTRUCTIONS *****

Choose a low integer (lowest being 0) and a high number more than 1 (and make it realistic not like 1 million or something, if you do just why?)
        
The computer will then choose a number between the highest and lowest numbers you selected. 
        
You then have to strategically guess the number the computer has chosen.
The less guesses the better.

Once you guess the number the computer will then respond 'higher or lower' depending on if the number it has chosen is higher or lower than your guess.

Press enter to lock in your guess 
                 <OR>
Use 'xxx' to quit the game.
        
        
        """)
  print()
  return""

# main routine starts here
played_before = yes_no("have you played before?")

if played_before == "no":
  print()
  instructions()

print ("program continues")