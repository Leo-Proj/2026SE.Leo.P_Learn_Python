answer = input("What is the answer to the Great Question of Life? ")

match answer:
    case "42" | "Forty Two" | "forty-two":
        print("Yes")
    case _:
        print("No")