x, y, z = input("Question? ").split()

x = int(x)
z = int(z)

if y == "+":
    result = (x + z)
elif y == "-":
    result = (x - z)
elif y == "x" or y == "*":
    result = (x * z)
elif result == "/":
    y == (x / z)
else:
    print("Math Error")
print(f"{result:.1f}")