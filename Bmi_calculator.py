# Write a program that calculates the body mass index from user's weight and height
# formula - BMI = weight / height^2
# Example input:
# 1.75
# 80
# Example output:
# 26

# 1st input: enter height in meters e.g: 1.75
height = input()

# 2nd input: enter weight in kilograms e.g: 80
weight = input()

new_height=float(height)
new_weight=int(weight)

bmi=(new_weight/new_height**2)

num3=int(bmi)
print(num3)