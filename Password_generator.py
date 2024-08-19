# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 4
# How many symbols would you like?
# 2
# How many numbers would you like?
# 2
# Your password is :

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# print,
# TbMH&%43 (o/p format - 4letters,2symbols,2numbers)
password=""

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print("Your password is : "+password)


# Or,


# print,
# 4b%Hu&3M
password_list = []

for char in range(1, nr_letters + 1):
  password_list+=random.choice(letters)

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)


random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print("Your password is: "+password)


