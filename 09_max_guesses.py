# HL component - maximum guesses calculator

import math

for item in range(0,4):    #loop component for easy testing

  low = int(input("Low: "))
  high = int(input("High: "))

  range = high - low + 1 
  max_raw = math.log2(range)
  max_upped = math.ceil(max_raw)
  max_guesses = max_upped + 1
  print("Max guesses: {}".format(max_guesses))

print()
