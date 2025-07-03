#define the functions needed, add, sub, mul, div
#print options to the users add, sub, mul, div
#ask for values
#call the functions
#while lop to continue the program until the users end

def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b
def div(a, b):
    if b == 0:
        return "X cannot be divided by zero!"
    return a / b