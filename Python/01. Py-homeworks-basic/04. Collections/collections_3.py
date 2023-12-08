queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

dictionary = {}

for meaning in queries:
    words = meaning.split()

    if len(words) in dictionary.keys():
        dictionary[len(words)] += 1
    else:
        dictionary.update({len(words):1})

for key, value in dictionary.items():
    percentage = round((value / len(queries)) * 100, 2)
    print(f'Запросов из {key} слов: {percentage}%')
