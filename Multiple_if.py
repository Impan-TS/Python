# Multiple if statements
# Print
# Welcome to the roller coaster!
# What is your height in cm? 122
# You can ride the roller coaster!
# What is your age? 34
# Adult tickets are $12.
# Do you want a photo taken? Y or N. Y
# Your final bill is $15


print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age > 18:
        bill = 12
        print("Adult tickets are $12.")

    else:
        bill = 7
        print("Youth tickets are $7.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
      bill+=3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
