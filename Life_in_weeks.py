#Write a program using maths and f-string that tells us how many weeks we have left, if we live until 90 years old.
# Example input,
# 56
# Example output,
# you have 1768 weeks left.

age = input()
new_age=int(age)

age1=(90-new_age)
age2=(age1*52)

print(f"You have {age2} weeks left.")