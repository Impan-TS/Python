# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 * 4) / 5 = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# Example Input,
# 3
# 9
# Example Output,
# You'll need 6 cans of paint.


import math

height = int(input())
width = int(input())
coverage = 5

def paint(h, w, c):
  can = (h * w) / c
  cans = math.ceil(can)
  print(f"You'll need {cans} cans of paint.")
paint(h=height, w=width, c=coverage)





