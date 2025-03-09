cost = 50
accepted_coins = [25, 10, 5]
amount_due = cost

while amount_due > 0:
    coin = int(input("Insert coin: "))
    
    if coin in accepted_coins:
        amount_due -= cost
    else:
        print("Insert a 25, 10 or 5 cent coin to continue")

    if amount_due > 0:
        print(f"Amount due: {amount_due}")

change = abs(amount_due)
if change >= 0:
    print(f"Change: {change}")