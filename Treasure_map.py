# Write a program that will mark a spot on a map with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# Example i/p,
# B3
# Example o/p,
# line1 = ['⬜️','⬜️','⬜️']
# line2 = ['⬜️','⬜️','⬜️']
# line3 = ['⬜️','X','⬜️']


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️","⬜️","⬜️"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input()

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")