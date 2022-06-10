#HL compontent - no duplicates

# to do
# set up empty list called already_guessed
# when user guesses, add guess to lists
# for each guess, check that number is not in already_guessed

# HL component - prevents duplicate guesses

secret = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed
num_won = 0 

guess = ""

while guess != secret and guesses_left >= 1:

  guess = int(input("guess: "))   # replace this with function

  #checks that guess is not a duplicate
  if guess in already_guessed:
    print("You already guessed that number! please try again "
         "You *still* have {} guesses left.".format(guesses_left))
    continue

  guesses_left -= 1
  already_guessed.append(guess)

  if guesses_left >= 1:

    if guess < secret:
      print("too low, try a higher number.  Guesses left: {}")

    elif guess > secret:
      print("too high, try a lower number.  Guesses left: {}")
  else:
    if guess < secret:
      print("too low!")
    elif guess > secret: 
      print("too high!")

if guess == secret:
  if guesses_left == guesses_allowed - 1:
    print("amazing! you got in less than {} guesses_allowed")
  else:
    print("well done, you got it in {} guesses. you have {} guesses_left")