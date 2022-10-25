def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greeting(func):
    greet = func("Hello all...")
    return greet

print(greeting(shout))
print(greeting(whisper))

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add = create_adder(10)
print(add(11))