def calculator (x,operator,y):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y
    else:
        return "Invalid operator"
x = 10
y = 5
operator = "-"
print(f"The result of {x} {operator} {y} is: {calculator(x, operator, y)}")