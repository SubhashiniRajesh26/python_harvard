def main():
    bill_amount()

def bill_amount():
    total = 0
    dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    while True:
        try:
            item = input("Item: ")
            item = item.title()
            # for k in dict:
            if item in dict:
                total += dict[item]
                print(f"Total: ${total:.2f}")
        except EOFError:
            break
        except KeyError:
            pass
    
             

main()