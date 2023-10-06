from pprint import pprint
cook_book = {}
list1 = list()
list2 = list()
with open('recipes.txt', encoding='utf-8') as file:
    for line in file:
        list1.append(''.join(line.strip().split('[]')))
    pprint(list1)
    dish_name = list1[0]
    number_of_ingredients = list1[1]

