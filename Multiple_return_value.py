# Multiple return value,

def name(fname,lname):
  if fname=="" or lname=="":
    return "empty inputs"

  name1=fname.title()
  name2=lname.title()

  return f"{name1} {name2}"

print(name("ROHIT","sharma"))

# OR

print(name(input("fname: "), input("lname: ")))