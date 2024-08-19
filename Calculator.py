# print,
# what is the first number ?: 7
# +
# -
# *
# /
# pickup an operation: +
# what's the next number?: 3
# 7.0+3.0=10.0
# type 'y' to continue calculating with 10.0, or type 'n' to start a new calculation : y
# pickup an operation: *
# what's the next number?: 2
# 10.0*2.0=20.0
# type 'y' to continue calculating with 10.0, or type 'n' to start a new calculation : n
# what is the first number ?:

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operation={
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
  }

def calculator():

    num1=float(input("what is the first number ?: "))

    for symbol in operation:
        print(symbol)

    should_continue=True

    while should_continue:
            operation_symbol=input("pickup an operation: ")
            num2=float(input("what's the next number?: "))
            calculation_function=operation[operation_symbol]
            answer=calculation_function(num1,num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            calculation=input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation : ").lower()
            if calculation=="y":
                num1=answer
            else:
                should_continue=False
                calculator()

calculator()