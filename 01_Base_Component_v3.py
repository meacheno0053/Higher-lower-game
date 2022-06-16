import random
import math

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

Choose a low integer (lowest being 1) and a high number being at least 10 or above. 
        
The computer will then choose a secret number between your two chosen numbers. 
        
the computer will calculate the number of guesses you are allowed.
The less guesses the better.

Once you guess the number the computer will then respond 'higher or lower' depending on if the number it has chosen is higher or lower than your guess.

Press enter to lock in your guess.
         <OR>
Use 'xxx' to quit the game.

Good Luck!
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

# Main routine  Starts here

# initialise whole game variables and lists
rounds_played = 0


# guess = int_check("Guess: ", lowest, highest, exit_code="xxx")

statement_generator("** Welcome to the Higher Lower Game **", "*", 3)
print()

played_before = yes_no("Have you played before?")

if played_before == "no":
  instructions()

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("How many rounds? <enter> for infinite ", 0, exit_code = "")

var_range = highest - lowest + 1 
max_raw = math.log2(var_range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1
print("Max guesses: {}".format(max_guesses))


num_won = 0

end_game = "no"
while end_game =="no":

  # Start of game play loop
  guesses_left = max_guesses
  
  # Rounds Heading
  print()
  if rounds =="":
    heading = "Continuous Mode: Round {}".format(rounds_played +1)
  else:
    heading = "Round {} of".format(rounds_played + 1, rounds)    

  
  print(heading)

  secret = random.randint(lowest, highest)
  print("spoiler alert!", secret) 
 
  run = True
while run :
    user_input = int(input('enter number: '))  # replace with function call when integrated
    if user_input == secret :
      print('you won!')
      run = False
    elif user_input < secret:
      print("Too High, try a lower number")
      
    else:
        print('try again!')

  
  # Guessing Loop

    guess = ""
    while guess != secret and guesses_left > 0:
  
      already_guessed = []

    guess = int_check("Guess", lowest, highest, "xxx")
    if guess == "xxx":
        end_game = "yes"
        break

    #checks that guess is not a duplicate
    if guess in already_guessed:
      print("You already guessed that number! Please try again "
           "You *still* have {} guesses left.".format(guesses_left))
      continue

    guesses_left = guesses_left - 1
    already_guessed.append(guess)
  
    if guesses_left >= 1:
  
      if guess < secret:
        print("Too low, try a higher number. Guesses left: {}".format(guesses_left))
  
      elif guess > secret:
        print("Too high, try a lower number. Guesses left: {}".format(guesses_left))
    else:
      if guess < secret:
        print("WHOOPS! Too low!  You have run out of guesses!")
      elif guess > secret: 
        print("WHOOPS! Too high! You have run out of guesses!")
  
    if guess == secret:
      if guesses_left > 1:
        print("Amazing! you got in less than {} guesses".format(max_guesses))
    else:
      print("Well done, you got it with {} guesses left.".format(already_guessed))
  
 
    rounds_played += 1
  
    # end game if requested # of rounds has been played
    if rounds_played == rounds:
      break

# Put end game content here
print("Thank you for playing")

# end game summary
