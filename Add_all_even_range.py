# Write a program to add up all even numbers from 1 to x.
# Example i/p,
# 10
# Example o/p,
# 30


num=int(input())
add=0
for number in range(2,num+1,2):
   add=add+number
print(add)