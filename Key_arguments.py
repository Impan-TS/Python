# Key arguments
def greet(name,loc,age):
    print(f"Hi {name}")
    print(f"Welcome {loc}")
    print(f"Age {age}")
greet(name="Ram",loc="Mysore",age=10)
greet(loc="Mysore",name="Ram",age=10)


# OR,

def greet(name,loc,age):
    print(f"Hi {loc}")
    print(f"Welcome {age}")
    print(f"Age {name}")
greet(name="Ram",loc="Mysore",age=10)