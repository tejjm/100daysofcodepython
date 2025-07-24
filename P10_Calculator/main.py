def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
calculator = {}
calculator["+"] = add
calculator["-"] = subtract
calculator["*"] = multiply
calculator["/"] = divide

from art import logo
print(logo)
condition = True
n1 = float(input("Enter the first number:\n"))
while condition:
    operator = str(input("Enter the operator you want to perform: +,-,*,/:\n"))
    n2 = float(input("Enter the second number:\n"))
    result = calculator[operator](n1,n2)
    print(f"The result of {n1} {operator} {n2} is {result}")
    continue_with_result = (input("Do you want to continue working with the previous result?:\n")).lower()
    if continue_with_result == "yes":
        n1 = result
    else: condition = False

