height=int(input("enter height"))

if height>120:
    print("can ride")

    age=int(input("enter age"))
    if age<=18:
        print("$7")
    else:
        print("$12")
else:
    print("can't ride")
