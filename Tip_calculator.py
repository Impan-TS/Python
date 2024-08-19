# Print
# Example output,
# welcome to the tip calculator.
# what was the total bill? $124.56
# what percentage would you like to give? 10, 12, or 15?12
# how many people to split the bill?7
# each person should pay: $19.93

input("welcome to the tip calculator.")
total_bill=float(input("what was the total bill? $"))
perc_tip=int(input("what percentage would you like to give? 10, 12, or 15?"))
people=int(input("how many people to split the bill?"))

new_perc_tip=perc_tip/100 * total_bill + total_bill
split_bill=new_perc_tip/people

result=round(split_bill,2)
print(f"each person should pay: ${result}")