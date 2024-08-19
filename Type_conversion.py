# We can only concatenate string (not a integer) to str
# So first we covert int into str and then concatenate it

num=len(input("what is your name "))
new_num=str(num)
print("your name contains "+new_num+" characters")