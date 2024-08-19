def name(fname, lname):
    """ Take a first and last name and format it to return the title case version of the name"""

    if fname == "" or lname == "":
        return "You didn't provide valid inputs"

    f_name = fname.title()
    l_name = lname.title()
    return f"Result: {f_name} {l_name}"

print(name(input("first_name : "), input("last_name : ")))
