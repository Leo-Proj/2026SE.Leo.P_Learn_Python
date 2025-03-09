num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operator = input("Operator: ")

if operator == "-":
    print(num1 - num2)
elif operator == "+":
    print(num1 + num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Not a known operator")