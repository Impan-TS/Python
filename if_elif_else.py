height=int(input("enter height"))

if height>120:
    print("can ride")

    age=int(input("enter age"))
    if age<12:
        print("$5")
    elif age>18:
        print("$12")
    else:
        print("$7")
else:
    print("can't ride")