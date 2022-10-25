from inflect import engine
p = engine()
while True:
    try:
        inp = input('Name: ')
        if inp == "Liesl":
            output = p.join(('Adieu', 'adieu', 'to', inp), final_sep = '', conj = '')
                
    except EOFError:
        print(output)
        break
