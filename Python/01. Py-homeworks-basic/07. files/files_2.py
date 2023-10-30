from pprint import pprint
cook_book = {}
with open('recipes.txt', 'rt', encoding='utf8') as file:
    for line in file:
        dish_name = line.strip()
        number = int(file.readline().strip())
        ingredient_list = list()
        for x in range(number):
            ingredients = {}
            ingredient = file.readline().strip()
            ingredients['ingredient_name'], ingredients['quantity'], ingredients['measure'] = ingredient.split('|')
            ingredients['quantity'] = int(ingredients['quantity'])
            ingredient_list.append(ingredients)
        file.readline()
        cook_book[dish_name] = ingredient_list

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for x in dishes:
        for j in cook_book[x]:
            result[j['ingredient_name']] = {'measure': j['measure'].strip(),
                                            'quantity': int(j['quantity']*person_count)}
    pprint(result)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

