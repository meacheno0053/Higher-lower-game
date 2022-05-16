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


statement_generator("** welcome to the higher lower game **", "*", 3)
print()