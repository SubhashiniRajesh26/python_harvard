threshold = 50
while(threshold > 0):
    print("Due amount: ", threshold)
    amount = int(input("insert coin: "))
    if(amount == 25 or amount == 10 or amount == 5):
        threshold = threshold - amount
    else:
        print("Due amount: 50")
print("change owed: ", abs(threshold))   