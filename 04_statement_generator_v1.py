# Decoration
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

# Main Routine goes here
statement_generator("** Welcome To The Higher Lower Game **", "*", 3)
