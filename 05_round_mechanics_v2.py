# Ask user for # of rounds then loop...
rounds_played = 0 

#intialise lost / drawn counters
rounds_drawn = 0
rounds_lost = 0

choose_instruction = "please choose an integer between the lowest chosen and the highest chosen"

# Ask user for # of rounds, <enter> for infinate mode
rounds = rounds_played ()

end_game = "no"
while end_game =="no":

  # Start of game play loop
  
  # Rounds Heading
  print()
  if rounds =="":
    heading = "Infinate Mode: Round {}".format(rounds_played +1)
  else:
    heading = "Round {} of {}".format(rounds_played + 1, rounds)    
    
  
  print(heading)
  choose_instruction = "Please choose rock (r), paper (p),scissors (s)"

  choice_error = "Please choose from rock " \
                  "paper / scissors (or xxx to quit)"
  
  # Ask user for choice and check it's valid
  user_choice = choice_checker("please choose an integer between the highest and lowest")
  if user_choice == "xxx":
    break
