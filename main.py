import calculator


def get_input():
    try:
        num1 = float(input("Weytin you wan calculate? : "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Weytin you wan calculate by? : "))
        return num1, op, num2
    except ValueError:
        print("X invalid input. Guy enter currect number. ")
        return get_input()
    
def main():

        print(" Welcome to Rattus Calculator App")
        num1, op, num2 = get_input()
        
        if op ==  "+":
            result = calculator.add(num1, num2)
        elif op == "-":
            result = calculator.sub(num1, num2)
        elif op == "*":
            result = calculator.mul(num1, num2)
        elif op == "/":
            result = calculator.div(num1, num2)
        else:
            result = "X oga put the right number. "
        print(f" result: {result}")
if __name__ == "__main__":
    main()