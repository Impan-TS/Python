# Python dictionary

dictionary={"name":"ravi",22:"age","gender":"male"}

# Retrieving item gender from dictionary,
print("Retrieving item : "+dictionary["gender"])


# Adding new items to dictionary,
dictionary["course"]="python"
print(f"Adding new items to dictionary : {dictionary}")


# Empty dictionary - wipe an existing dictionary,
dictionary={}
print(f"Empty dictionary : {dictionary}")


dictionary={"name":"ravi",22:"age","gender":"male","course": "python"}

# Edit an item in dictionary
dictionary["name"]="ram"
print(f"Edit an item in dictionary : {dictionary}")


# for loop through a dictionary,
for dict in dictionary:
   print(f"for loop through a dictionary : {dict}")


for dict in dictionary:
   print(f"for loop through a dictionary key : {dict}")
   print(f"for loop through a dictionary value : {dictionary[dict]}")
