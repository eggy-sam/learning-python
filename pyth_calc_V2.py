from re import X




def calculate(operator,x ,y):
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    elif operator == "x":
        print(x * y)
    elif operator == "/":
        print(x / y)
    else:
        print(f"unknown {operator} ")
        


calculate(str(input("Choose operator (+, -, x, /): ")), float(input("First No: ")), float(input("Second No: ")))