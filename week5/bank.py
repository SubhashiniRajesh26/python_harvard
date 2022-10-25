def value(greeting):
    if "hello" in greeting or "Hello" in greeting:
        return "$0"
    elif greeting.startswith("h") or greeting.startswith("H"):
        return "$20"
    else:
        return "$100"

def main():
    greeting = input("Enter your Greeting: ")
    print(value(greeting))

if __name__ == "__main__":
    main()