def sum(a,b):
    add = a + b
    return add
def diff(a,b):
    diff = a - b
    return diff
def multiply(a,b):
    mult = a * b
    return mult
def divide(a,b):
    if b == 0:
        return ZeroDivisionError
    div = a / b
    return div
def calc():
    numA = int(input("enter a num"))
    num = int(input("Enter a 2nd Number: "))
    