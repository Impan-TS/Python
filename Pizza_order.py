# To build an automatic pizza order program.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
# Example Input,
# L
# Y
# N
# Example Output,
# Your final bill is: $28.


size=input("Enter size: s,m or l")
add_pepperoni=input("Enter y or n")
extra_cheese=input("Enter y or n")

if size=="s":
    bill=15

elif size=="m":
        bill=20

else:
        bill=25

if add_pepperoni=="y":
    if size=="s":
        bill+=2

    else:
        bill+=3

if extra_cheese=="y":
    bill+=1

print(f"Your final bill is: ${bill}")