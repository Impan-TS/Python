# Project - Treasure Island
#
# Print,
# Welcome to Treasure Island. Your mission is to find the treasure.
# Enter the direction, "left" or "right" LEFT
# Enter you'r option, "wait" or "swim" wait
# Enter which door, "red" or "blue" or "yellow" yellow
# You win


 # ('''
 # *******************************************************************************
 #           |                   |                  |                     |
 #  _________|________________.=""_;=.______________|_____________________|_______
 # |                   |  ,-"_,=""     `"=.|                  |
 # |___________________|__"=._o`"-._        `"=.______________|___________________
 #           |                `"=._o`"=._      _`"=._                     |
 #  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
 # |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
 # |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
 #           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 #  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
 # |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
 # |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
 # ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
 # /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
 # ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
 # /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
 # ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
 # /______/______/______/______/______/______/______/______/______/______/
 # *******************************************************************************
 # ''')


print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice_1=input('Enter the direction, "left" or "right"').lower()

if choice_1=="left":

    choice_2 = input('Enter you\'r option, "wait" or "swim"').lower()
    if choice_2=="wait":

        choice_3=input('Enter which door, "red" or "blue" or "yellow"').lower()
        if choice_3=="red":
            print("Burned by fire. Game Over.")

        elif choice_3=="blue":
            print("Eaten by beasts. Game Over.")

        elif choice_3=="yellow":
            print("You win")

        else:
            print("Anything else. Game over")

    else:
        print("Attacked by trout. Game over")

else:
    print("Fail into a hole. Game over")