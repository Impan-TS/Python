# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."

# Example i/p,
# Angela Yu
# Jack Bauer

# Example o/p,
# Your score is 53.


name1 = input()
name2 = input()

name=name1+" "+name2

new_name=name.lower()

T=new_name.count("t")
R=new_name.count("r")
U=new_name.count("u")
E=new_name.count("e")
true=T+R+U+E

L=new_name.count("l")
O=new_name.count("o")
V=new_name.count("v")
E=new_name.count("e")
love=L+O+V+E

str_true=str(true)
str_love=str(love)

str_love_score=str_true+str_love

int_love_score=int(str_love_score)

if int_love_score<10 or int_love_score>90:
  print("Your score is "+str_love_score+", you go together like coke and mentos.")

elif int_love_score>40 and int_love_score<50:
  print("Your score is "+str_love_score+", you are alright together.")

else:
  print("Your score is "+str_love_score+".")