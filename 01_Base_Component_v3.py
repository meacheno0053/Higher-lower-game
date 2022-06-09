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

Choose a low integer (lowest being 0) and a high number being at least 10 or above. 
        
The computer will then choose a number between the highest and lowest numbers selected. 
        
You then have to strategically guess the number the computer has chosen.
The less guesses the better.

Once you guess the number the computer will then respond 'higher or lower' depending on if the number it has chosen is higher or lower than your guess.

Press enter to lock in your guess.
         <OR>
Use 'xxx' to quit the game.
        
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


def int_check(question, low=None, high=None, exit_code = None):

  situation = ""

  if low is not None and high is not None:
    situation = "both"
  elif low is not None and high is None:
    situation = "low only"

  while True:

    response = input(question)

    if response == exit_code:
      return response

    try:
      response = int(response)

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



# Main routine  Starts here

# initialise whole game variables and lists
rounds_played = 0


# guess = int_check("Guess: ", lowest, highest, exit_code="xxx")

statement_generator("** welcome to the higher lower game **", "*", 3)
print()

played_before = yes_no("have you played before?")

if played_before == "no":
  instructions()

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("How many rounds? <enter> for infinite", 0, exit_code = "")

end_game = "no"
while end_game =="no":

  # Start of game play loop

  
  # Rounds Heading
  print()
  if rounds =="":
    heading = "Continuous Mode: Round {}".format(rounds_played +1)
  else:
    heading = "Round {} of".format(rounds_played + 1, rounds)    

  
  print(heading)

  guess = input()
  if guess == "xxx":
      end_game = "yes"
      break
  
 
  rounds_played += 1

  # end game if requested # of rounds has been played
  if rounds_played == rounds:
    break

# Put end game content here
print("Thank you for playing")