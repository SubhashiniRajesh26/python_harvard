from datetime import datetime
def my_decorator(func):
    def wrapper():
        print("Something happened before a function call")
        func()
        print("Something happened after a function call")
    return wrapper

def say_whee():
    print("Whee!")

def not_during_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass 
    return wrapper

# say_whee = my_decorator(say_whee)
# say_whee()

say_whee = not_during_night(say_whee)
say_whee()
