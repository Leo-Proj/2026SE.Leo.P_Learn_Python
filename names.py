names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")








#name = input("what's your name? ")

#with open("names.txt", "a") as file:
    #file.write(f"{name}\n")




#names = []

#for _ in range(3):
    #names.append(input("what's your name? "))

#for name in sorted(names):
    #print(f"hello, {name}")