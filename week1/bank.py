def dollorForGreeting(greeting):
    if "hello" in greeting or "Hello" in greeting:
        print("$0")
    elif greeting.startswith("h") or greeting.startswith("H"):
        print("$20")
    else:
        print("$100")

def main():
    greeting = input("Enter your Greeting")
    dollorForGreeting(greeting)


main()