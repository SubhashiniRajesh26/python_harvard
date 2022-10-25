import random
while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            continue
        number = random.randint(0, level)
    except ValueError:
        continue
    
    while True:
        try:
            guess = int(input("Guess: "))
            if((guess or number) < 0):
                continue
            else:
                if(guess < number):
                    print("Too small!")
                elif(guess > number):
                    print("Too large!")
                else:
                    print("Just right!")
                    break

        except ValueError:
            pass
    break