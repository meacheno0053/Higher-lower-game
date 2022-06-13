import random

hl_list = ["guess", "lowest", "highest", "xxx"]

for item in range(0,20):
  comp_choice = random.choice(hl_list[:-1])
  print(comp_choice, end="\t")