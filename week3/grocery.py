def main():
    count_item()


def count_item():
    dict = {}
    while True:
        try:
            item = input().upper()
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1
        except EOFError:
            break
        except KeyError:
            pass

    
    for k in sorted(dict.keys()):
        print(dict[k], k)


main()