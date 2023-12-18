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
    print(cook_book)