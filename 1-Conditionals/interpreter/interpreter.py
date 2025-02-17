x, y, z = int(input("Question? ")).split()

x = int(x)
z = int(z)

if y == "+":
    result = (x + y)
elif y == "-":
    result = (x - y)
elif y == "x" or y == "*":
    result = (x * y)
elif result == "/":
    y == (x / y)
else:
    print("Math Error")