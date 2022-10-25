def main():
    fruit = input("Enter the friut name to get calories: ")
    print(calories(fruit.title()))



def calories(fruit):
    dict = {
        'Apple' : 130, 'Avocado' : 50, 'Banana' : 110, 'Cantaloupe' : 50, 'Grape Fruit' : 60, 'Honeydew Melon' : 50,
        'Kiwi Fruit' : 90, 'Lemon' : 15, 'Lime' : 20, 'Nectarine' : 60, 'Peach' : 60, 'Pear' : 100, 'Pineapple' : 50,
        'Plums' : 70, 'Strawberries' : 50, 'Sweet Cherries' : 100, 'Tangerine' : 50, 'Water Melon' : 80
    }
    for k in dict:
        if k == fruit:
            return dict[k]

main()