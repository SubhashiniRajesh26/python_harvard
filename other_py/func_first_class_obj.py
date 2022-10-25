def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

mylist = [say_hello, be_awesome]
# print(mylist[0]("Subhashini"))


def greet_subha(greeter_func):
    return greeter_func("Subhashini")

print(greet_subha(say_hello))
print(greet_subha(be_awesome))