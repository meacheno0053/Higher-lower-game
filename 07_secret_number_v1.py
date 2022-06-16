import random

secret = random.randint(lowest, highest)
print("spoiler alert", secret)

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
