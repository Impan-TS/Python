# Positional arguments
def greet(name,loc,age):
    print(f"Hi {name}")
    print(f"Welcome {loc}")
    print(f"Age {age}")
greet("Ram","Mysore",10)
greet("Mysore","Ram",10)


# OR,

def greet(name,loc,age):
    print(f"Hi {loc}")
    print(f"Welcome {age}")
    print(f"Age {name}")
greet("Ram","Mysore",10)